labs = {
    1: "Lab_1/Lab_1.py",
    2: "Lab_1/Lab_2.py",
    3: "Lab_1/Lab_3.py",
    4: "Lab_1/Lab_4.py"
}

print('------ Labs ------')
print('1. Lab 1')
print('2. Lab 2')
print('3. Lab 3')
print('4. Lab 4')

try:
    # Отримання вибору користувача
    choose = int(input('Choose your lab (1-4): '))

    if choose in labs:
        with open(labs[choose], "r") as file:  # Відкриваємо обраний файл
            code = file.read()  # Читаємо його вміст
            exec(code)  # Виконуємо код із файлу
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
except ValueError:
    print("Invalid input. Please enter a number.")
except FileNotFoundError as e:
    print(f"Error: {e}")
