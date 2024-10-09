import graphviz

# Створюємо стильне дерево рішень за допомогою Graphviz
decision_tree = graphviz.Digraph('Investment Decision Tree', format='png')

# Додаємо стилі для вузлів
decision_tree.attr('node', shape='box', style='filled', color='lightblue', fontname='Helvetica', fontsize='10')

# Перше рішення - Чекати чи ні
decision_tree.node('Q', 'Чекати чи ні?\n(Імовірність: 1)')
decision_tree.node('N', 'Не чекати\nОцінка: 212500\nІмовірність: 1')
decision_tree.edge('Q', 'N', label='Не чекати')

# Вибір заводу, якщо не чекати
decision_tree.node('L', 'Великий завод\nВартість: 600000\nОчикуваний прибуток: 200000\nІмовірність: 0.7')
decision_tree.node('L_N', 'Великий завод\nВартість: 600000\nОчикуваний прибуток: -850000\nІмовірність: 0.3')
decision_tree.node('M', 'Малий завод\nВартість: 350000\nОчикуваний прибуток: 400000\nІмовірність: 0.7')
decision_tree.node('M_N', 'Малий завод\nВартість: 350000\nОчикуваний прибуток: -225000\nІмовірність: 0.3')
decision_tree.edge('N', 'L', label='Великий')
decision_tree.edge('N', 'L_N', label='Великий (негативний)')
decision_tree.edge('N', 'M', label='Малий')
decision_tree.edge('N', 'M_N', label='Малий (негативний)')

# Чекати найкращі варіанти
decision_tree.node('W', 'Чекати\nОцінка: 244000\nІмовірність: 1')
decision_tree.edge('Q', 'W', label='Чекати')

# Прогноз позитивний
decision_tree.node('P', 'Позитивні прогнози\nОцінка: 280000\nІмовірність: 0.8')
decision_tree.edge('W', 'P', label='Позитивні')

# Вибір заводу при позитивному прогнозі
decision_tree.node('L_P', 'Великий завод\nОчикуваний прибуток: 400000\nІмовірність: 0.9')
decision_tree.node('M_P', 'Малий завод\nОчикуваний прибуток: 250000\nІмовірність: 0.9')
decision_tree.edge('P', 'L_P', label='Великий')
decision_tree.edge('P', 'M_P', label='Малий')

# Прогноз негативний
decision_tree.node('NP', 'Негативні прогнози\nОцінка: 100000\nІмовірність: 0.2')
decision_tree.edge('W', 'NP', label='Негативні')

# Вибір заводу при негативному прогнозі
decision_tree.node('L_NP', 'Великий завод\nОчикуваний прибуток: 40000\nІмовірність: 0.1')
decision_tree.node('M_NP', 'Малий завод\nОчикуваний прибуток: -250000\nІмовірність: 0.1')
decision_tree.edge('NP', 'L_NP', label='Великий')
decision_tree.edge('NP', 'M_NP', label='Малий')

# Додати кольори до різних типів вузлів
decision_tree.attr('node', shape='box', style='filled', fontname='Helvetica', fontsize='10')
decision_tree.node('L', color='lightcoral')
decision_tree.node('M', color='lightgreen')
decision_tree.node('W', color='lightyellow')
decision_tree.node('P', color='lightblue')
decision_tree.node('NP', color='lightgrey')
decision_tree.node('L_P', color='lightcoral')
decision_tree.node('M_P', color='lightgreen')
decision_tree.node('L_N', color='lightcoral')
decision_tree.node('M_N', color='lightgreen')
decision_tree.node('L_NP', color='lightcoral')
decision_tree.node('M_NP', color='lightgreen')

# Зберегти граф
decision_tree.render('full_decision_tree')


