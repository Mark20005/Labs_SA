import numpy as np
import pandas as pd
# Матриця платежів
matrix = np.array([
    [100, 15 ],
    [0  , 115],
    [50 , 45 ]
])


# Середня вартість маршрутів
mean_cost = np.mean(matrix, axis=0)
matrix_pd = pd.DataFrame(matrix, columns=['A', 'B'], index=['A', 'B', '50/50'])
matrix_pd.loc['avg_func'] = list(mean_cost)
print(matrix_pd,'\n')
print("Стратегія 0 - слід обрати маршрут А")
print("Стратегія 1 - слід обрати маршрут В")
print("Джеку слід дотримуватися стратегії", np.argmin(mean_cost))
