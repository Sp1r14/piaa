import sys

def mask_to_cities(mask, n):
    return [i for i in range(n) if (mask & (1 << i))]

def alsh1_approximate(graph, n):
    visited = [False] * n
    current_city = 0
    visited[current_city] = True
    path = [current_city]
    total_cost = 0

    print(f"  [АЛШ-1] Старт. Текущий город: {current_city}")

    for step in range(n - 1):
        best_next_city = -1
        min_dist = float('inf')
        
        print(f"  [АЛШ-1] Шаг {step + 1}. Ищем куда пойти из города {current_city}:")
        
        for v in range(n):
            if not visited[v] and graph[current_city][v] > 0:
                cost = graph[current_city][v]
                print(f"    -> Дорога в город {v} стоит {cost}")
                
                if cost < min_dist:
                    min_dist = cost
                    best_next_city = v
                    
        if best_next_city == -1:
            print("  [АЛШ-1] Тупик! Дальше пути нет.")
            return float('inf'), []
            
        print(f"  [АЛШ-1] Выбираем самую дешевую: идем в город {best_next_city} за {min_dist}\n")
            
        visited[best_next_city] = True
        path.append(best_next_city)
        total_cost += min_dist
        current_city = best_next_city

    return_cost = graph[current_city][0]
    if return_cost > 0:
        total_cost += return_cost
        path.append(0)
        print(f"  [АЛШ-1] Все города пройдены. Возврат из {current_city} в 0 стоит {return_cost}")
        return total_cost, path
    else:
        return float('inf'), []

def solve():
    data = (open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()).split()
    if not data: return

    n = int(data[0])
    graph = [[int(data[i*n + j + 1]) for j in range(n)] for i in range(n)]

    print(" АЛШ-1 (Приближенный метод) ")
    print("-"*50)
    
    approx_cost, approx_path = alsh1_approximate(graph, n)
    if approx_cost == float('inf'):
        print("\nИТОГ АЛШ-1: no path")
    else:
        print(f"\nИТОГ АЛШ-1: {approx_cost}")
        print("Маршрут: " + " -> ".join(map(str, approx_path)))
    print("\n") 

    print(" ДП (Точный метод) ")
    print("-"*50)
    print("  [ДП] Начинаем погружение в рекурсию...\n")
    
    memo = [[-1] * n for _ in range(1 << n)]
    nxt_node = [[-1] * n for _ in range(1 << n)]

    def tsp_dp(mask, u):
        if mask == (1 << n) - 1:
            cost = graph[u][0]
            print(f"  [ДП] Базовый случай: все города посещены. Возврат из {u} в 0 стоит {cost if cost > 0 else 'НЕТ ПУТИ'}")
            if cost > 0:
                return cost
            return float('inf')
            
        if memo[mask][u] != -1:
            cities = mask_to_cities(mask, n)
            print(f"  [ДП] Кэш: для города {u} при посещенных {cities} ответ уже известен: {memo[mask][u]}")
            return memo[mask][u]

        ans = float('inf')
        best_nxt = -1

        for v in range(n):
            if not (mask & (1 << v)) and graph[u][v] > 0:
                res = graph[u][v] + tsp_dp(mask | (1 << v), v)
                if res < ans:
                    ans = res
                    best_nxt = v
                    
        memo[mask][u] = ans
        nxt_node[mask][u] = best_nxt
        
        cities = mask_to_cities(mask, n)
        if best_nxt != -1:
            print(f"  [ДП] Запись в кэш: Из города {u} (посещены {cities}) оптимально идти в {best_nxt}. Оценка остатка: {ans}")
            
        return ans

    min_cost = tsp_dp(1, 0)

    if min_cost == float('inf'):
        print("\nИТОГ ДП: no path")
    else:
        print(f"\nИТОГ ДП: {min_cost}")
        
        path = [0]
        mask = 1
        u = 0
        while mask != (1 << n) - 1:
            v = nxt_node[mask][u]
            path.append(v)
            mask |= (1 << v)
            u = v
        path.append(0)
        
        print("Маршрут: " + " -> ".join(map(str, path)))

if __name__ == '__main__':
    solve()