def get_distances(s, t):
    N, M = len(s), len(t)
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    for j in range(1, M + 1):
        dp[0][j] = j
        print(f"Ячейка 0,{j}: пустая строка -> '{t[:j]}' (+ вставка)")
            
    for i in range(1, N + 1):
        dp[i][0] = i
        print(f"Ячейка {i},0: '{s[:i]}' -> пустая строка (+ удаление)")
        
        for j in range(1, M + 1):
            c = s[i-1] != t[j-1]
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + c)
            
            if not c:
                op = f"== '{t[j-1]}' -> без изменений (из {i-1},{j-1})"
            elif dp[i][j] == dp[i-1][j-1] + 1:
                op = f"!= '{t[j-1]}' -> замена (из {i-1},{j-1})"
            elif dp[i][j] == dp[i-1][j] + 1:
                op = f"!= '{t[j-1]}' -> удаление (из {i-1},{j})"
            else:
                op = f"!= '{t[j-1]}' -> вставка (из {i},{j-1})"
            print(f"Ячейка {i},{j}: '{s[i-1]}' {op}")
    
    print()
    for row in dp: print(row)
    return [dp[i][M] for i in range(N + 1)]

def solve():
    s, t = input().strip(), input().strip()

    print("--- ПРЯМОЙ ПРОХОД (ПРЕФИКСЫ) ---")
    p_dists = get_distances(s, t)
    
    print("\n--- ОБРАТНЫЙ ПРОХОД (СУФФИКСЫ) ---")
    s_dists = get_distances(s[::-1], t[::-1])

    min_p, min_s = min(p_dists), min(s_dists)
    
    print("\nИтоговое расстояние:", p_dists[-1])
    print("\nМинимальное расстояние (префиксы):", min_p)
    for i, d in enumerate(p_dists):
        if d == min_p: print(f"  '{s[:i] or '(пустая строка)'}'")

    print("Минимальное расстояние (суффиксы):", min_s)
    for i, d in enumerate(s_dists):
        if d == min_s: print(f"  '{s[len(s)-i:] or '(пустая строка)'}'")

if __name__ == '__main__':
    solve()