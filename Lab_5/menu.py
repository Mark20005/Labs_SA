labs = {
    1: "Lab_5/5_1_10.py",
    2: "Lab_5/5_2_10.py",

}

print('------ Labs ------')
print('1. Lab 5 - Task 1')
print('2. Lab 5 - Task 2')

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