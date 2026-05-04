def solve_cyclic_shift():
    try:
        a = input()
        b = input()
    except EOFError:
        return

    n = len(a)
    m = len(b)

    print(f"\n[СТАРТ] Проверка циклического сдвига: A = '{a}', B = '{b}'")
    if n != m:
        print("Длины строк не равны. Они не могут быть сдвигом друг друга.")
        print("\n[РЕЗУЛЬТАТ]\n-1")
        return
    if n == 0:
        print("\n[РЕЗУЛЬТАТ]\n0")
        return

    print(f"\n[ЭТАП 1] Вычисляем префикс-функцию для шаблона B = '{b}'")
    pi = [0] * m
    j = 0
    for i in range(1, m):
        print(f"  Символ B[{i}] = '{b[i]}', сравниваем с B[{j}] = '{b[j]}'")
        while j > 0 and b[i] != b[j]:
            j = pi[j - 1]
            print(f"Не совпало. Откат j: j = {j}")
        if b[i] == b[j]:
            j += 1
            print(f"Совпало! j = {j}")
        pi[i] = j
    print(f"Итоговый pi-массив для B: {pi}\n")

    print(f"[ЭТАП 2] Ищем B в зацикленной строке A")
    j = 0
    for i in range(2 * n - 1):
        char_a = a[i % n]
        print(f"  Шаг {i}: Виртуальный символ A[{i} % {n}] = '{char_a}', Шаблон B[{j}] = '{b[j] if j < m else 'вне границ'}'")
        
        while j > 0 and char_a != b[j]:
            j = pi[j - 1]
            print(f" Не совпало. Откат j: j = {j}")
        if char_a == b[j]:
            j += 1
            print(f" Совпало! Увеличиваем j до {j}")
            
        if j == m:
            ans = i - m + 1
            print(f" НАЙДЕНО! Строка B найдена внутри сдвоенной A!")
            print(f"\n[РЕЗУЛЬТАТ]")
            print(ans)
            return

    print("\n[РЕЗУЛЬТАТ]")
    print("-1")

if __name__ == '__main__':
    solve_cyclic_shift()