import graphviz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Функція для створення DataFrame та обчислення очікуваних доходів
def calculate_expected_returns(data: dict) -> pd.DataFrame:
    df = pd.DataFrame(data)
    df['Expected Return'] = df['Probability'] * df['Total Return']
    expected_returns = df.groupby('Investment')[['Expected Return']].sum()
    return expected_returns

# Функція для відображення інформації про доходи
def display_expected_returns(expected_returns: pd.DataFrame) -> None:
    print("Expected returns for each option:")
    print(expected_returns)
    max_min_diff = expected_returns['Expected Return'].max() - expected_returns['Expected Return'].min()
    print(f'Альтернатива з інвестування у фонд є вигіднішою на {max_min_diff} гривень')

# Функція для створення стилізованого дерева рішень
def create_stylized_decision_tree(final_bonds: float, final_fund: float) -> graphviz.Digraph:
    dot = graphviz.Digraph('Stylized Decision Tree', format='png')

    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica', fontsize='12', color='black')
    dot.attr('edge', fontname='Helvetica', fontsize='10', color='gray')

    # Root node
    dot.node('0', 'Куди вкласти 100,000 грн?', fillcolor='lightblue', style='filled')

    # Облігації
    dot.node('1', 'Облігації', fillcolor='lightyellow', style='filled')
    dot.node('2', 'Фонд', fillcolor='lightgreen', style='filled')

    dot.edge('0', '1', label='Облігації', color='blue', penwidth='2')
    dot.edge('0', '2', label='Фонд', color='green', penwidth='2')

    dot.node('1.1', 'Зростання: 118,800', fillcolor='yellow', style='filled')
    dot.node('1.2', 'Спад: 111,300', fillcolor='yellow', style='filled')
    dot.node('1.3', 'Незмінність: 107,500', fillcolor='yellow', style='filled')
    dot.edge('1', '1.1', label='Ймовірність 20%', color='blue', style='dashed')
    dot.edge('1', '1.2', label='Ймовірність 15%', color='blue', style='dashed')
    dot.edge('1', '1.3', label='Ймовірність 65%', color='blue', style='dashed')

    dot.node('1.4', f'Цільова функція: {final_bonds:.2f}', fillcolor='lightgray', style='filled')
    dot.edge('1.1', '1.4', color='gray50')
    dot.edge('1.2', '1.4', color='gray50')
    dot.edge('1.3', '1.4', color='gray50')

    # Фонд
    dot.node('2.1', 'Зростання: 121,200', fillcolor='green', style='filled')
    dot.node('2.2', 'Спад: 121,200', fillcolor='green', style='filled')
    dot.node('2.3', 'Незмінність: 109,080', fillcolor='green', style='filled')
    dot.edge('2', '2.1', label='Ймовірність 20%', color='green', style='dashed')
    dot.edge('2', '2.2', label='Ймовірність 15%', color='green', style='dashed')
    dot.edge('2', '2.3', label='Ймовірність 65%', color='green', style='dashed')

    dot.node('2.4', f'Цільова функція: {final_fund:.2f}', fillcolor='lightgray', style='filled')
    dot.edge('2.1', '2.4', color='gray50')
    dot.edge('2.2', '2.4', color='gray50')
    dot.edge('2.3', '2.4', color='gray50')

    return dot

# Функція для розрахунку функції корисності
def utility_function(x: np.ndarray, a: float, b: float) -> np.ndarray:
    return 1 - np.exp(-a * (x - b) / np.max(np.abs(x - b)))

# Функція для візуалізації функції корисності
def plot_utility(x_values: np.ndarray, y_cautious: np.ndarray, y_neutral: np.ndarray, y_risk_loving: np.ndarray) -> None:
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y_cautious, label="Обережний інвестор (X-облігації)", color='blue', linestyle='--')
    plt.plot(x_values, y_neutral, label="Нейтральний інвестор (Y)", color='green', linestyle='-')
    plt.plot(x_values, y_risk_loving, label="Схильний до ризику (Z-фонд)", color='red', linestyle=':')

    plt.title('Функція корисності для різних інвесторів')
    plt.xlabel('Тисячі доларів')
    plt.ylabel('Корисність (Utility)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Дані для обчислень
data = {
    'Investment': ['Облігації', 'Облігації', 'Облігації', 'Фонд', 'Фонд', 'Фонд'],
    'Inflation': ['зростання', 'спад', 'незмінність', 'зростання', 'спад', 'незмінність'],
    'Probability': [0.20, 0.15, 0.65, 0.20, 0.15, 0.65],
    'Nominal Price': [100000, 100000, 100000, 100000, 100000, 100000],
    '% Return': [0.08, 0.06, 0.075, 0.01, 0.01, 0.01],
    'Nominal Price Change': [0.10, 0.05, 0.00, 0.20, 0.20, 0.08],
    'Total Return': [118800, 111300, 107500, 121200, 121200, 109080]
}

# Розрахунок і відображення очікуваних доходів
expected_returns = calculate_expected_returns(data)
display_expected_returns(expected_returns)

# Розрахунок кінцевих функцій для облігацій та фонду
final_bonds = (0.20 * 118800) + (0.15 * 111300) + (0.65 * 107500)
final_fund = (0.20 * 121200) + (0.15 * 121200) + (0.65 * 109080)

# Створення і рендеринг стилізованого дерева рішень
styled_decision_tree = create_stylized_decision_tree(final_bonds, final_fund)
styled_decision_tree.render('decision_tree', format='png', cleanup=True)

# Візуалізація функції корисності для різних типів інвесторів
x_values = np.linspace(-20000, 40000, 500)
y_cautious = utility_function(x_values, 0.5, 10000)
y_neutral = utility_function(x_values, 1, 10000)
y_risk_loving = utility_function(x_values, 2, 10000)

plot_utility(x_values, y_cautious, y_neutral, y_risk_loving)
