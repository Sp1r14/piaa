import time

def solve_square_iterative(N):
    if N == 1:
        print(f"N = 1, тривиальный случай — один квадрат 1x1")
        return [(1, 1, 1)]

    p = N
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            p = i
            break
    m = N // p

    if p != N:
        print(f"Найден наименьший делитель p = {p}, применяем масштаб x{m}")
        print(f"Задача сведена к квадрату {p}x{p}")
    else:
        print(f"N = {N} является простым числом, масштабирование невозможно")
        print(f"Запускаем полный перебор для квадрата {p}x{p}")

    if p == 2:
        print(f"Чётный размер столешницы — делим на 4 квадрата размером {m}x{m}")
        squares = [(0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
        return [(x * m + 1, y * m + 1, w * m) for x, y, w in squares]

    half = p // 2
    first_sq = half + 1

    print(f"\nРазмещаем три начальных квадрата:")
    print(f"  Квадрат {first_sq}x{first_sq} в левый верхний угол (0, 0)")
    print(f"  Квадрат {half}x{half} справа от первого ({first_sq}, 0)")
    print(f"  Квадрат {half}x{half} снизу от первого (0, {first_sq})")

    cols = [p] * half + [first_sq] + [half] * half
    best_sol = []
    min_count = [p * p]
    current_sol = [
        (0, 0, first_sq),
        (first_sq, 0, half),
        (0, first_sq, half)
    ]
    stack = []

    iteration = 0  

    while True:
        min_y = min(cols)
        min_x = cols.index(min_y)

        need_backtrack = False

        if min_y == p:
            print(f"\n  Все клетки заняты!")
            if len(current_sol) < min_count[0]:
                min_count[0] = len(current_sol)
                best_sol = list(current_sol)
                print(f"  Новый рекорд: {min_count[0]} квадратов")
            need_backtrack = True

        elif len(current_sol) >= min_count[0]:
            print(f"  Количество квадратов ({len(current_sol)}) >= текущего минимума ({min_count[0]}) — отсечение")
            need_backtrack = True

        if need_backtrack:
            while stack:
                last_x, last_y, last_w, last_max_w = stack.pop()

                for i in range(last_x, last_x + last_w):
                    cols[i] -= last_w
                current_sol.pop()

                new_w = last_w - 1
                if new_w > 0:
                    print(f"  Откат: уменьшаем квадрат в позиции ({last_x}, {last_y}) с {last_w} до {new_w}")
                    for i in range(last_x, last_x + new_w):
                        cols[i] += new_w
                    current_sol.append((last_x, last_y, new_w))
                    stack.append([last_x, last_y, new_w, last_max_w])
                    break
                else:
                    print(f"  Квадрат в позиции ({last_x}, {last_y}) исчерпан — извлекаем следующий из стека")
            else:
                print(f"\nСтек пуст — перебор завершён")
                break
            continue

        max_w = 1
        for i in range(min_x + 1, p):
            if cols[i] == min_y:
                max_w += 1
            else:
                break
        max_w = min(max_w, p - min_y)

        iteration += 1
        print(f"\nИтерация {iteration}: свободная позиция ({min_x}, {min_y}), "
              f"размещаем квадрат {max_w}x{max_w}, "
              f"всего квадратов в решении: {len(current_sol) + 1}")

        for i in range(min_x, min_x + max_w):
            cols[i] += max_w
        current_sol.append((min_x, min_y, max_w))
        stack.append([min_x, min_y, max_w, max_w])

    print(f"\nЛучшее найденное решение: {min_count[0]} квадратов")
    print(f"Применяем масштаб x{m} и переводим координаты ")

    result = []
    for x, y, w in best_sol:
        rx, ry, rw = x * m + 1, y * m + 1, w * m
        print(f"  ({x}, {y}, {w}) -> ({rx}, {ry}, {rw})")
        result.append((rx, ry, rw))

    return result


def solve_and_time(N):
    print(f"Начало работы программы, N = {N}")
    print("\n")

    start = time.perf_counter()
    result = solve_square_iterative(N)
    end = time.perf_counter()

    print("\n")
    print(f"Результат работы программы:")
    print(len(result))
    for x, y, size in result:
        print(f"{x} {y} {size}")
    print(f"\nВремя выполнения: {end - start:.6f} секунд")


if __name__ == "__main__":
    solve_and_time(int(input()))