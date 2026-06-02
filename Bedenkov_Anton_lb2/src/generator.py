import random
n = int(input("Количество городов: "))
name = input("Имя файла (Enter для input.txt): ") or "input.txt"

with open(name, 'w') as f:
    f.write(f"{n}\n")
    f.write("\n".join(" ".join(str(random.randint(1, 50) if i != j and random.random() > 0.1 else 0) for j in range(n)) for i in range(n)))