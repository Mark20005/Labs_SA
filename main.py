labs = {
    1: "Lab_1/menu.py",
    2: "Lab_2/Lab_2.py",
    3: "Lab_3/menu.py",
    4: "Lab_4/Lab_4.py"
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
        with open(labs[choose], "r", encoding='UTF-8') as file:
            code = file.read()
            exec(code)
    else:
        print("Invalid choice. Please choose a number between 1 and 4.")
except ValueError:
    print("Invalid input. Please enter a number.")
except FileNotFoundError as e:
    print(f"Error: {e}")
