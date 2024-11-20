def print_table(k, R, dp, allocation, profit_row):
    # Формуємо заголовки стовпців
    print (f"k = {k}")
    header = f"|    | " + " | ".join([f"{i:>3} " for i in range(R + 1)]) + f"| F{k}(C{k}) | x*{k} |"
    print(header)
    print("----" + "----" * (R + 9))  # Розділитель між заголовком і даними

    # Формуємо кожен рядок таблиці
    for r in range(R + 1):
        row = f"| {r:>2} | "  # Початковий стовпець для кожного рядка
        row += " | ".join(
            [f"{profit_row[x] + dp[k - 1][r - x]:>4.1f}" if x <= r else " -- " for x in range(R + 1)]
        )  # Додаємо розраховані значення або "-"
        row += f"|{dp[k][r]:>6.1f}  |{allocation[k][r]:>3}  |"
        print(row)
    print("\n")

def print_profit_table(profit_table):
    # Заголовки стовпців
    header = "|\tx\t| " + " | ".join([f"{i:>4}" for i in range(len(profit_table[0]))]) + " |"
    print(header)
    print("-" * len(header))  # Розділитель

    # Виведення кожного рядка таблиці
    for i, row in enumerate(profit_table):
        row_str = f"| g{i+1}(x) | " + " | ".join([f"{value:>4.1f}" for value in row]) + " |"
        print(row_str)
    print("\n")

# Прибутки для кожного підприємства
profit_table = [
    [0, 1.2, 1.6, 3.4, 4.0, 5.2],  # g1(x)
    [0, 0.8, 1.3, 2.0, 3.6, 4.9],  # g2(x)
    [0, 0.5, 1.0, 2.3, 2.9, 4.1]   # g3(x)
]

def maximize_profit_with_steps(profit, n, R):
    # Таблиці DP і відновлення розподілу
    dp = [[0] * (R + 1) for _ in range(n + 1)]
    allocation = [[0] * (R + 1) for _ in range(n + 1)]

    # Початок розрахунку з підприємства k = 3
    for i in range(n, 0, -1):  # Проходимо з k = 3 до k = 1
        for r in range(R + 1):  # Для кожного обсягу ресурсу
            for x in range(r + 1):  # Кількість ресурсу для поточного підприємства
                current_profit = profit[i - 1][x] + dp[i - 1][r - x]
                if current_profit > dp[i][r]:
                    dp[i][r] = current_profit
                    allocation[i][r] = x
        # Виведення таблиці після кожного етапу
        print_table(i, R, dp, allocation, profit[i - 1])

    # Відновлення оптимального розподілу
    X = [0] * n
    remaining_resource = R
    for i in range(n, 0, -1):
        X[i - 1] = allocation[i][remaining_resource]
        remaining_resource -= X[i - 1]

    return dp[n][R], X


n = 3  # Кількість підприємств
R = 5  # Загальна кількість ресурсів (млн грн)

# Обчислення з виведенням етапів
print_profit_table(profit_table)
max_profit, optimal_allocation = maximize_profit_with_steps(profit_table, n, R)

print("Максимальний сумарний дохід:", max_profit)
print("Оптимальний розподіл коштів між підприємствами (в млн грн):", optimal_allocation)
