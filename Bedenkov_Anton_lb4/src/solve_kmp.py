def solve_kmp():
    try:
        p = input()
        t = input()
    except EOFError:
        return

    if not p:
        print("-1")
        return

    m = len(p)
    n = len(t)

    print(f"\n[ЭТАП 1] Вычисляем префикс-функцию для шаблона P = '{p}'")
    pi = [0] * m
    j = 0
    for i in range(1, m):
        print(f"  Символ P[{i}] = '{p[i]}', сравниваем с P[{j}] = '{p[j]}'")
        while j > 0 and p[i] != p[j]:
            j = pi[j - 1]
            print(f"Не совпало. Откат указателя j по pi-массиву: j = {j}")
        if p[i] == p[j]:
            j += 1
            print(f"Совпало! Увеличиваем j до {j}")
        pi[i] = j
        print(f"Записываем pi[{i}] = {j}")
    print(f"Итоговый pi-массив: {pi}\n")

    print(f"[ЭТАП 2] Начинаем поиск шаблона P в тексте T = '{t}'")
    res = []
    j = 0
    for i in range(n):
        print(f"  Шаг i={i}: Текст T[{i}] = '{t[i]}', Шаблон P[{j}] = '{p[j] if j < m else 'вне границ'}'")
        while j > 0 and t[i] != p[j]:
            j = pi[j - 1]
            print(f"Не совпало. Откат j по pi-массиву: j = {j}")
        if t[i] == p[j]:
            j += 1
            print(f" Совпало! Двигаемся дальше по шаблону, j = {j}")
        if j == m:
            start_index = i - m + 1
            print(f"НАЙДЕНО ПОЛНОЕ ВХОЖДЕНИЕ! Индекс начала: {start_index} ")
            res.append(str(start_index))
            # Откат для поиска перекрывающихся вхождений
            j = pi[j - 1]
            print(f"Откат j для поиска возможных наложений: j = {j}")

    print("\n[РЕЗУЛЬТАТ]")
    print(",".join(res) if res else "-1")

if __name__ == '__main__':
    solve_kmp()