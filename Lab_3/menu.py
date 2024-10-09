labs = {
    1: "Lab_3/Lab_3_5.py",
    2: "Lab_3/Lab_3_12.py",
    3: "Lab_3/Lab_3_man.py"
}

print('------ Labs ------')
print('1. Lab 3 - Task 5')
print('2. Lab 3 - Task 12')
print('3. Lab 3 - Task 12 - manual years')

try:

    choose = int(input('Choose task: '))

    if choose in labs:
        with open(labs[choose], "r", encoding='UTF-8') as file:
            code = file.read()
            exec(code)
    else:
        print("Invalid choice. Please choose 1, 2 or 3.")
except ValueError:
    print("Invalid input. Please enter a number.")
except FileNotFoundError as e:
    print(f"Error: {e}")