labs = {
    1: "Lab_1/Lab_1_man.py",  # Лабораторна з ручним введенням
    2: "Lab_1/Lab_1_import.py"  # Лабораторна зі зчитуванням з файлу Excel
}

print('------ Labs ------')
print('1. Lab 1 - Manual Input')
print('2. Lab 1 - Read from Excel')

try:

    choose = int(input('Choose your lab (1-2): '))

    if choose in labs:
        with open(labs[choose], "r") as file:
            code = file.read()
            exec(code)
    else:
        print("Invalid choice. Please choose 1 or 2.")
except ValueError:
    print("Invalid input. Please enter a number.")
except FileNotFoundError as e:
    print(f"Error: {e}")