import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


shifts = [8, 6, 10]  # Тривалість змін
max_hours = [10, 8, 12]  # Максимальний робочий час для працівників

# Створення таблиці витрат
cost_matrix = np.array([[8, 6, np.inf],  # Працівник A
                        [8, 6, np.inf],  # Працівник B
                        [8, 6, 10]])  # Працівник C

# Створимо таблицю для виведення
workers = ['A', 'B', 'C']
shift_names = ['Зміна 1 ', 'Зміна 2 ', 'Зміна 3 ']
df = pd.DataFrame(cost_matrix, index=workers, columns=shift_names)


# Функція для виконання угорського методу
def hungarian_algorithm(cost_matrix):
    # Зменшення рядків
    cost_matrix = cost_matrix - cost_matrix.min(axis=1).reshape(-1, 1)

    # Зменшення стовпців
    cost_matrix = cost_matrix - cost_matrix.min(axis=0)

    # Призначення змін за допомогою викреслювання ліній
    n = len(cost_matrix)
    row_cover = [False] * n
    col_cover = [False] * n
    starred_zeros = np.zeros((n, n))
    primed_zeros = np.zeros((n, n))

    # Покроковий процес (це реалізація одного з варіантів угорського методу)
    def step_1():
        # Вибір нулів в кожному стовпці, які можна покрити
        for i in range(n):
            for j in range(n):
                if cost_matrix[i][j] == 0 and not row_cover[i] and not col_cover[j]:
                    starred_zeros[i][j] = 1
                    row_cover[i] = True
                    col_cover[j] = True

    step_1()

    # Показати результат роботи
    return cost_matrix, starred_zeros


# Виконання угорського методу для нашої матриці витрат
result_matrix, starred_zeros = hungarian_algorithm(cost_matrix)

# Перетворення результату в DataFrame для кращого відображення
result_df = pd.DataFrame(starred_zeros, index=workers, columns=shift_names)

# Вивести таблицю з результатами
print("Початкова таблиця витрат:")
print(df)

print("\nРезультати угорського методу (Покриття зірочками):")
print(result_df)

# Побудуємо графік для відображення розподілу змін
fig, ax = plt.subplots()
cax = ax.matshow(starred_zeros, cmap="Blues")

# Додамо текст до клітинок
for (i, j), value in np.ndenumerate(starred_zeros):
    if value == 1:
        ax.text(j, i, f'{workers[i]} -> {shift_names[j]}', ha='center', va='center', color='black', fontsize=10)

# Оформлення графіка
ax.set_xticks(np.arange(len(shift_names)))
ax.set_yticks(np.arange(len(workers)))
ax.set_xticklabels(shift_names)
ax.set_yticklabels(workers)
plt.title("Призначення змін працівникам")
plt.xlabel("Зміни")
plt.ylabel("Працівники")
plt.colorbar(cax)

plt.show()