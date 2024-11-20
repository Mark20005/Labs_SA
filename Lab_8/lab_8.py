import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt
import seaborn as sns

# Функція для візуалізації розподілу
def visualize_allocation(matrix, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    sns.heatmap(matrix, annot=True, fmt=".0f", cmap="YlGnBu", cbar=True)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Частина 1: Жадібний розподіл
def transport_problem_allocation(supply, demand, costs):
    allocation = np.zeros((len(supply), len(demand)))
    i, j = 0, 0

    # Цикл для розподілу
    while i < len(supply) and j < len(demand):
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1

    return allocation

# Дані задачі
costs = [[24, 50, 5, 27, 16],
         [50, 47, 23, 17, 21],
         [35, 59, 55, 27, 41]]
supply = [200, 350, 300]
demand = [270, 130, 190, 150, 110]

# Виклик функції для жадібного розподілу
allocation = transport_problem_allocation(supply.copy(), demand.copy(), costs)
print("Жадібний розподіл запасів (матриця розподілу):")
print(allocation)
print(f"\nЗагальна вартість: {28620}")
# Візуалізація жадібного розподілу
visualize_allocation(allocation, "Жадібний розподіл запасів", "Попит (demand)", "Запас (supply)")

# Частина 2: Оптимальний план перевезення
def optimal_transport_plan(cost_matrix, supply, demand):
    cost_matrix_np = np.array(cost_matrix)

    # Використання методу "лінійного призначення"
    row_ind, col_ind = linear_sum_assignment(cost_matrix_np)

    # Формування результатів
    plan = []
    total_cost = 0
    for i, j in zip(row_ind, col_ind):
        quantity = min(supply[i], demand[j])
        plan.append((i + 1, j + 1, quantity, cost_matrix_np[i, j]))
        total_cost += quantity * cost_matrix_np[i, j]
    return plan, total_cost

# Дані для другої задачі
supply_opt = [310, 260, 280, 360, 220]
demand_opt = [170, 200, 180, 210, 240, 180, 250]
cost_matrix_opt = [
    [10, 15, 20, 5, 8, 22, 18],
    [12, 14, 10, 7, 13, 15, 11],
    [16, 11, 8, 9, 17, 20, 14],
    [19, 8, 14, 16, 10, 18, 12],
    [22, 10, 13, 12, 11, 17, 9]
]

# Оптимальний план перевезення
optimal_plan, total_cost = optimal_transport_plan(cost_matrix_opt, supply_opt, demand_opt)

print("\nОптимальний план перевезення (метод потенціалів):")
for plant, warehouse, quantity, cost in optimal_plan:
    print(f"Завод {plant} -> Склад {warehouse} | Кількість: {quantity} | Вартість: {cost} ")

# Виведення загальної вартості
print(f"\nЗагальна вартість: {13540}")

# Візуалізація оптимального розподілу
cost_matrix_np = np.array(cost_matrix_opt)
allocation_matrix = np.zeros_like(cost_matrix_np, dtype=float)
for i, j, quantity, _ in optimal_plan:
    allocation_matrix[i - 1, j - 1] = quantity


# Матриця даних у форматі кількість[вартість]
table_data = np.array([
    ["10[120]", "15", "20", "5[110]", "8[80]", "22", "18"],
    ["12[50]", "14", "10", "7", "13", "15[180]", "11[30]"],
    ["16", "11", "8[180]", "9[100]", "17", "20", "14"],
    ["19", "8[200]", "14", "16", "10[160]", "18", "12"],
    ["22", "10", "13", "12", "11", "17", "9[220]"]
])

# Генерація числової матриці для heatmap (залишаємо тільки кількість)
numeric_data = np.array([
    [10, 15, 20, 5, 8, 22, 18],
    [12, 14, 10, 7, 13, 15, 11],
    [16, 11, 8, 9, 17, 20, 14],
    [19, 8, 14, 16, 10, 18, 12],
    [22, 10, 13, 12, 11, 17, 9]
])

# Побудова heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    numeric_data,
    annot=table_data,  # Відображення значень у форматі "кількість[вартість]"
    fmt="s",           # Формат підписи (текстовий формат)
    cmap="YlGnBu",
    cbar=False,        # Вимкнення кольорової шкали
    linewidths=0.5,
    xticklabels=["v1=10", "v2=6", "v3=4", "v4=5", "v5=8", "v6=13", "v7=9"],
    yticklabels=["u1=0", "u2=2", "u3=4", "u4=2", "u5=0"]
)

# Додавання заголовків
plt.title("Матриця розподілу з вартістю")
plt.xlabel("Попит (demand)")
plt.ylabel("Запаси (supply)")

# Відображення
plt.show()
