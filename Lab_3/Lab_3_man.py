import pandas as pd
import numpy as np
from graphviz import Digraph


def calc(data, term):
    cost = np.array([data["big_factory"]["cost"], data["small_factory"]["cost"]])
    comm = np.array(data["commodity"])

    big_income = np.array(data["big_factory"]["income"])
    big_value = big_income * term - cost[0]
    big_value = np.sum(big_value * comm)

    small_income = np.array(data["small_factory"]["income"])
    small_value = small_income * term - cost[1]
    small_value = np.sum(small_value * comm)

    return big_value, small_value


# Вхідні дані
data = {
    "not_wait": {
        "commodity": [0.7, 0.3],
        "big_factory": {
            "cost": 600_000,
            "income": [250_000, -50_000],
        },
        "small_factory": {
            "cost": 350_000,
            "income": [150_000, 25_000],
        },
    },
    "wait": {
        "forecats_probability": [0.8, 0.2],
        "positive_forecast": {
            "commodity": [0.9, 0.1],
            "big_factory": {
                "cost": 600_000,
                "income": [250_000, -50_000],
            },
            "small_factory": {
                "cost": 350_000,
                "income": [150_000, 25_000],
            },
        },
        "negative_forecast": {
            "commodity": [0.7, 0.3],
            "big_factory": {
                "cost": 600_000,
                "income": [250_000, -50_000],
            },
            "small_factory": {
                "cost": 350_000,
                "income": [150_000, 25_000],
            },
            "no_factory": {
                "cost": 0,
                "income": 0,
            },
        },
    }
}

# Введення терміна інвестування
term = float(input("Введіть термін для інвестування: "))

# Рішення не чекати
not_wait_big_value, not_wait_small_value = calc(data["not_wait"], term)
not_wait_max_value = max(not_wait_big_value, not_wait_small_value)

# Рішення чекати
# У випадку позитивних прогнозів
positive_big_value, positive_small_value = calc(data["wait"]["positive_forecast"], term - 1)
# У випадку негативних прогнозів
negative_big_value, negative_small_value = calc(data["wait"]["negative_forecast"], term - 1)

# Розрахунок цільової функції для чекання
wait_value = (
        positive_big_value * data["wait"]["forecats_probability"][0] +
        negative_small_value * data["wait"]["forecats_probability"][1]
)

# Створення графа
dot = Digraph(format='png')

# Додаємо стилі
dot.attr('node', shape='box', style='filled', fontname='Helvetica', fontsize='12')
dot.attr('edge', fontname='Helvetica', fontsize='10')

# Додаємо вузли
dot.node('A', 'Вибір', fillcolor='lightblue')
dot.node('B', 'Не чекати\nЦільова функція: {:.2f}'.format(not_wait_max_value), fillcolor='lightgreen')
dot.node('C', 'Чекати\nЦільова функція: {:.2f}'.format(wait_value), fillcolor='lightyellow')
dot.node('D1', 'Великий завод\nПрибуток: {:.2f}'.format(not_wait_big_value), fillcolor='lightcoral')
dot.node('D2', 'Малий завод\nПрибуток: {:.2f}'.format(not_wait_small_value), fillcolor='lightcoral')
dot.node('E1', 'Позитивні прогнози\nВеликий завод\nПрибуток: {:.2f}'.format(positive_big_value), fillcolor='lightgreen')
dot.node('E2', 'Малий завод\nПрибуток: {:.2f}'.format(positive_small_value), fillcolor='lightgreen')
dot.node('F1', 'Негативні прогнози\nВеликий завод\nПрибуток: {:.2f}'.format(negative_big_value), fillcolor='lightcoral')
dot.node('F2', 'Малий завод\nПрибуток: {:.2f}'.format(negative_small_value), fillcolor='lightcoral')
dot.node('G', 'Не будувати нічого\nПрибуток: 0', fillcolor='lightgray')

# Додаємо ребра
dot.edge('A', 'B', 'Обрати')
dot.edge('A', 'C', 'Обрати')
dot.edge('B', 'D1', 'Вибрати великий')
dot.edge('B', 'D2', 'Вибрати малий')
dot.edge('C', 'E1', 'Позитивний прогноз')
dot.edge('C', 'E2', 'Позитивний прогноз')
dot.edge('C', 'F1', 'Негативний прогноз')
dot.edge('C', 'F2', 'Негативний прогноз')
dot.edge('F1', 'G', 'Не прибутковий')
dot.edge('F2', 'G', 'Не прибутковий')

# Візуалізація графа
dot.render('investment_decision_tree', format='png', cleanup=True)  # Виведе в PNG файл
dot.view()


# Обчислення цільової функції для гілки
def decor():
    print("-------------------------------------------------------------------")


def calc(data, term):
    cost = np.array([data["big_factory"]["cost"], data["small_factory"]["cost"]])
    comm = np.array(data["commodity"])

    # Розрахунок середнього прибутку для великого заводу
    big_income = np.array([data["big_factory"]["income"]])
    big_value = big_income * term - cost[0]
    big_value = np.sum(big_value * comm)

    # Розрахунок середнього прибутку для малого заводу
    small_income = np.array([data["small_factory"]["income"]])
    small_value = small_income * term - cost[1]
    small_value = np.sum(small_value * comm)
    # print(big_value, small_value, big_income*term-cost[0], small_income*term-cost[1], comm)
    # Вирішуємо який завод збудувати на основі максимального прибутку
    if big_value >= small_value:
        return big_value, "великий"
    else:
        return small_value, "малий"


data = pd.DataFrame(
    {
        "not_wait": {
            "commodity": [0.7, 0.3],
            "big_factory": {
                "cost": 600_000,
                "income": [250_000, -50_000],
            },
            "small_factory": {
                "cost": 350_000,
                "income": [150_000, 25_000],
            },
        },

        "wait": {
            "forecats_probability": [0.8, 0.2],

            "positive_forecast": {
                "commodity": [0.9, 0.1],
                "big_factory": {
                    "cost": 600_000,
                    "income": [250_000, -50_000],
                },
                "small_factory": {
                    "cost": 350_000,
                    "income": [150_000, 25_000],
                },

            },

            "negative_forecast": {
                "commodity": [0.7, 0.3],
                "big_factory": {
                    "cost": 600_000,
                    "income": [250_000, -50_000],
                },
                "small_factory": {
                    "cost": 350_000,
                    "income": [150_000, 25_000],
                },
                "no_factory": {
                    "cost": 0,
                    "income": 0,
                },
            },
        }
    }
)


# Рішення не чекати
not_wait_value, not_wait_fabric = calc(data["not_wait"], term)

# Рішення почекати
# У випадку позитивних прогнозів
positive_value, positive_fabric = calc(data["wait"]["positive_forecast"],
                                       term - 1)  # Оскільки ми чекаємо рік, то термін для прибутку буде на 1 менше
# У випадку негативних прогнозів
negative_value, negative_fabric = calc(data["wait"]["negative_forecast"], term - 1)
# Якщо для негативних прогнозів заводи неприбуткові - нічого не будуємо
if negative_value < 0:
    negative_value = 0
    negative_fabric = "ніякий"

print("Якщо не чекатимемо, то краще побудувати", not_wait_fabric,
      "завод. Значення функції за вказаний термін становить: ", not_wait_value)
print()
print("Якщо чекатимемо і будуть позитивні прогнози, то краще побудувати", positive_fabric,
      "завод. Значення функції за вказаний термін становить: ", positive_value)
print()
print("Якщо чекатимемо і будуть негативні прогнози, то краще побудувати", negative_fabric,
      "завод. Значення функції за вказаний термін становить: ", negative_value)
print()

# Розраховуємо вибір якщо чекатимемо.
if positive_value < 0 and negative_value == 0:
    # На вказаний термін будуть тільки збитки - нічого не будуємо
    wait_value = 0
    wait_fabric = negative_fabric
else:
    prob = np.array(data["wait"]["forecats_probability"])
    wait_value = np.array([positive_value, negative_value])
    wait_value = np.sum(wait_value * prob)
    # Яку фабрику будуватимемо при чеканні
    if positive_fabric == negative_fabric:
        wait_fabric = positive_fabric
    else:
        # Якщо фабрики в обох варіантах різняться - вирішемо потім, після перевірки прогнозу
        wait_fabric = "вирішимо на основі прогнозу"

if wait_value > not_wait_value:
    final_value = wait_value
    final_fabric = wait_fabric
else:
    final_value = not_wait_value
    final_fabric = not_wait_fabric
print("Отже, якщо чекатимемо, то значення функції буде становити: ", final_value)

print("\n\nОСТАТОЧНЕ РІШЕННЯ!")

decor()
if wait_value > not_wait_value:
    print("Ми зачекаємо. Який побудувати завод? - ", final_fabric, ". Значення функції: ", final_value)
else:
    print("Будуємо ", final_fabric, " негайно! Значення функції ", final_value)
decor()
