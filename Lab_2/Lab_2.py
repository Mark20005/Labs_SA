import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sympy import Matrix, pprint

def geomean(arr):
    return np.exp(np.mean(np.log(arr), axis=len(arr.shape)-1))

def normalize(arr):
    _sum = np.sum(arr, axis=len(arr.shape)-1)
    return arr/_sum

def criteria_sum(arr):
    return np.sum(arr, axis=0)

# Створення матриць парних порівнянь
comparisons = {
    "C1": [
      [1, 3, 5, 7, 9, 2, 4],
      [1/3, 1, 4, 6, 8, 1/2, 1/3],
      [1/5, 1/4, 1, 3, 5, 1/4, 1/5],
      [1/7, 1/6, 1/3, 1, 4, 1/5, 1/7],
      [1/9, 1/8, 1/5, 1/4, 1, 1/6, 1/9],
      [1/2, 2, 4, 5, 6, 1, 2],
      [1/4, 3, 5, 7, 9, 1/2, 1]
    ],
    "C2": [
      [1, 2, 4, 6, 8, 3, 5],
      [1/2, 1, 3, 5, 7, 1/2, 2],
      [1/4, 1/3, 1, 2, 4, 1/3, 1/2],
      [1/6, 1/5, 1/2, 1, 3, 1/4, 1/3],
      [1/8, 1/7, 1/4, 1/3, 1, 1/5, 1/4],
      [1/3, 2, 3, 4, 5, 1, 3],
      [1/5, 1/2, 2, 3, 4, 1/3, 1]
    ]
}

# Введення експертних оцінок для альтернатив
criteria = {
    "price": [
        [[1.0, 3.0, 3/10], [1/3, 1.0, 1/5], [10/3, 5.0, 1.0]],
        [[1.0, 3.0, 1/5], [1/3, 1.0,1/3], [5.0, 3.0, 1.0]]
    ],
    "quality": [
        [[1.0, 1/5,1/3], [5.0, 1.0, 3.0], [3.0,1/3, 1.0]],
        [[1.0, 1/5, 1/5], [5.0, 1.0, 3.0], [5.0,1/3, 1.0]]
    ],
    "brand": [
        [[1.0,1/3, 5.0], [3.0, 1.0, 1/5], [1/5, 5.0, 1.0]],
        [[1.0,1/3, 3.0], [3.0, 1.0, 1/5], [0.33, 5.0, 1.0]]
    ],
    "functionality": [
        [[1.0, 5.0,1/3], [1/5, 1.0, 3.0], [3.0,1/3, 1.0]],
        [[1.0, 5.0, 3.0], [1/5, 1.0, 1/5], [1/3, 3.0, 1.0]]
    ],
    "ergonomics": [
        [[1.0, 3.0,1/3], [0.33, 1.0, 5.0], [3.0, 1/5, 1.0]],
        [[1.0, 5.0,1/3], [1/5, 1.0, 3.0], [3.0,1/3, 1.0]]
    ],
    "reliability": [
        [[1.0, 5.0,1/3], [1/5, 1.0, 3.0], [3.0,1/3, 1.0]],
        [[1.0, 3.0,1/3], [1/3, 1.0, 1/5], [3.0, 5.0, 1.0]]
    ],
    "safety": [
        [[1.0, 1/5,1/3], [5.0, 1.0, 3.0], [3.0,1/3, 1.0]],
        [[1.0, 3.0, 1/5], [1/3, 1.0, 3.0], [5.0, 1/5, 1.0]]
    ]
}

# Функція для обчислення нормалізованих ваг для кожного критерію
def calculate_normalized_weights(criteria_dict):
    norm_weights_1, norm_weights_2 = [], []
    for key, matrices in criteria_dict.items():
        W_norm_1 = normalize(geomean(np.array(matrices[0])))
        W_norm_2 = normalize(geomean(np.array(matrices[1])))
        norm_weights_1.append(W_norm_1)
        norm_weights_2.append(W_norm_2)
    return np.vstack(norm_weights_1), np.vstack(norm_weights_2)

# Обчислення глобальних критеріїв
C1, C2 = np.array(comparisons["C1"]), np.array(comparisons["C2"])
W_norm_C1, W_norm_C2 = normalize(geomean(C1)), normalize(geomean(C2))

W_norm_all_1, W_norm_all_2 = calculate_normalized_weights(criteria)

# Альтернативи A1, A2, A3
A1 = np.max(np.vstack([W_norm_all_1[:, 0], W_norm_all_2[:, 0]]), axis=0)
A2 = np.max(np.vstack([W_norm_all_1[:, 1], W_norm_all_2[:, 1]]), axis=0)
A3 = np.max(np.vstack([W_norm_all_1[:, 2], W_norm_all_2[:, 2]]), axis=0)

MO = geomean(np.vstack([W_norm_C1, W_norm_C2]).T)

global_criteria = [np.sum(MO * A1), np.sum(MO * A2), np.sum(MO * A3)]

# Виведення результатів
print("MO")
pprint(Matrix(MO))

print("A1")
pprint(Matrix(A1))

print("A2")
pprint(Matrix(A2))

print("A3")
pprint(Matrix(A3))

print("Global")
pprint(Matrix(global_criteria))

print("Choose alternative with biggest global_criteria: ")
print("A", global_criteria.index(max(global_criteria)) + 1, " = ", max(np.round(global_criteria, decimals=2)), sep="")

global_df = pd.DataFrame(global_criteria, index=["A1", "A2", "A3"], columns=["Global"])

def show_global(df):
    gl_cr = sns.barplot(x=df.index, y="Global", data=df, hue="Global", palette="deep", errorbar=None)
    plt.xlabel('Alternatives')
    gl_cr.set_title("Global Criteria")
    return plt.show()

show_global(global_df)

# Дані для прикладу
labels = ['K1 - Price', 'K2 - Quality', 'K3 - Brand', 'K4 - Functionality', 'K5 - Ergonomics', 'K6 - Reliability', 'K7 - Safety', 'Global']

# Кількість змінних
num_vars = len(labels)

A1_1 = list(A1)
A1_1.append(global_criteria[0])
A2_1 = list(A2)
A2_1.append(global_criteria[1])
A3_1 = list(A3)
A3_1.append(global_criteria[2])
# Створюємо кутову координатну сітку
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # замкнути форму

# Замкнути графік
A1_1 += A1_1[:1]
A2_1 += A2_1[:1]
A3_1 += A3_1[:1]

# Налаштування графіка
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Налаштування відображення осей
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Встановлюємо мітки для кожної змінної
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Встановлюємо межі по радіусу (0-1)
ax.set_ylim(0, 1)

# Додаємо графіки для кожної альтернативи
ax.plot(angles, A1_1, linewidth=2, linestyle='solid', label='A1', color='blue')
ax.fill(angles, A1_1, color='blue', alpha=0.25)

ax.plot(angles, A2_1, linewidth=2, linestyle='solid', label='A2', color='green')
ax.fill(angles, A2_1, color='green', alpha=0.25)

ax.plot(angles, A3_1, linewidth=2, linestyle='solid', label='A3', color='red')
ax.fill(angles, A3_1, color='red', alpha=0.25)

# Додаємо легенду
ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.show()