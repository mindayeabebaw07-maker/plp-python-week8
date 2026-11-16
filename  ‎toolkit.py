# Week 8 Final Project - My Toolkit
# A menu-driven program with 3 tools: Calculator, To-Do List, Number Explorer

# List to store tasks - it changes while program runs
tasks = []

def show_menu():
    print("\n===== MY TOOLKIT =====")
    print("1. Simple Calculator")
    print("2. To-Do List Manager")
    print("3. Number Explorer")
    print("4. Quit")
    print("======================")

def calculator():
    print("\n--- Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Choose: +  -  *  /")
        op = input("Enter operation: ")

        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Oops! You cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operation. Please use + - * /")
    except ValueError:
        print("Please enter numbers only!")

def todo_list():
    print("\n--- To-Do List Manager ---")
    while True:
        print("\nYour tasks:", tasks if tasks else "No tasks yet!")
        print("a. Add task")
        print("b. Remove task")
        print("c. Back to main menu")
        choice = input("Choose a, b or c: ").lower()

        if choice == "a":
            task = input("Enter new task: ")
            tasks.append(task)
            print(f"Added: {task}")
        elif choice == "b":
            if not tasks:
                print("List is empty, nothing to remove.")
            else:
                task = input("Enter task to remove: ")
                if task in tasks:
                    tasks.remove(task)
                    print(f"Removed: {task}")
                else:
                    print("That task is not in the list.")
        elif choice == "c":
            break
        else:
            print("Please choose a, b or c.")

def number_explorer():
    print("\n--- Number Explorer ---")
    print("Enter numbers one by one. Type 'done' to finish.")
    numbers = []
    while True:
        entry = input("Enter a number (or 'done'): ")
        if entry.lower() == "done":
            break
        try:
            numbers.append(int(entry))
        except ValueError:
            print("Please enter a whole number or 'done'.")

    if not numbers:
        print("You didn't enter any numbers.")
        return

    print(f"\nYour numbers: {numbers}")
    print(f"Total numbers: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Average: {sum(numbers) / len(numbers):.2f}")
    print(f"Biggest: {max(numbers)}")
    print(f"Smallest: {min(numbers)}")

    print("\nEven or Odd:")
    for n in numbers:
        if n % 2 == 0:
            print(f"{n} is Even")
        else:
            print(f"{n} is Odd")

# Main program loop - runs until user quits
while True:
    show_menu()
    choice = input("Choose 1, 2, 3 or 4: ")

    if choice == "1":
        calculator()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        number_explorer()
    elif choice == "4":
        print("\nThanks for using My Toolkit! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3 or 4.")