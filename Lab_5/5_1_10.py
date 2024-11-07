import numpy as np
import pandas as pd

# Задана матриця платежів
payoff_matrix = np.array([
    [-3, 2, 9, 6],
    [-2, 5, 4, 6],
    [5, 3, 1, -5],
    [8, -2, 8, 4]
])


# Знаходимо найбільше значення в кожному рядку (нижні ціни гри)
lower_prices = np.min(payoff_matrix, axis=1)

# Знаходимо найменше значення в кожному стовпчику (верхні ціни гри)
upper_prices = np.max(payoff_matrix, axis=0)

lower_price = np.max(lower_prices)
upper_price = np.min(upper_prices)

maxmin_indexes = np.where(lower_prices == lower_price)
minmax_indexes = np.where(upper_prices == upper_price)


payoff_matrix_pd = pd.DataFrame(payoff_matrix, columns=['B1','B2','B3', 'B4'], index=['A1','A2','A3','A4'])
payoff_matrix_pd['min_A'] = lower_prices
payoff_matrix_pd.loc['max_В'] = list(upper_prices) + [None]
print(payoff_matrix_pd)
print("Lower Price (Нижня ціна гри):", lower_price)
print("Upper Price (Верхня ціна гри):", upper_price)

# Перевіряємо, чи існують рівноваги в чистих стратегіях
if lower_price == upper_price:
    pure_strategy_equilibria = np.argwhere(payoff_matrix == np.max(lower_prices))
    print("Pure Strategy Equilibria (Рівноваги в чистих стратегіях, сідлова точка):", pure_strategy_equilibria)
else:
    print(f"Рівновага в чистих стратегіях для даного випадку відсутня, сідлова точка: {-1}")