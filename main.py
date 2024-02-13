def list_names(students):
    index = 1
    for student in students:
        print(f"{index}. {student['name']}")
        index += 1

def get_new_student():
    name = input("Please input a name for the new student:\n")
    hometown = input("Next please input their hometown:\n")
    favorite_food = input("Last please input their favorite food:\n")
    return {"name": name, "hometown": hometown, "favorite_food": favorite_food}

def main():
    students = [
        {'name': 'Cole Jenkins', 'hometown': 'Rock Hill SC', 'Favorite Food': 'Sushi'},
        {'name': 'Sam Arewood', 'hometown': ' Mobile AL', 'Favorite Food': 'Fried Chicken'},
        {'name': 'Fionna DaVinci', 'hometown': ' Los Angeles CA', 'Favorite Food': 'Pizza'}
    ]

    while True:
        print("Please select which action you'd like to do: add, view, or quit")
        action = input("> ").lower()

        if action == 'add':
            new_student = get_new_student()
            students.append(new_student)
            print("Student added successfully!")
        elif action == 'view':
            list_names(students)
            while True:
                choice = input("Which student would you like to learn more about? Enter a number 1-" + str(len(students)) + ":\n> ")
                if choice.isdigit():
                    index = int(choice) - 1
                    if 0 <= index < len(students):
                        student = students[index]
                        print(f"Student {index+1} is {student['name']}. What would you like to know?")
                        info = input("Enter 'hometown' or 'favorite food':\n> ").lower()
                        if info == 'hometown':
                            print(f"{student['name']} is from {student['hometown']}")
                            break
                        elif info == 'favorite food':
                            print(f"{student['name']}'s favorite food is {student['favorite_food']}")
                            break
                        else:
                            print("Invalid option! Please enter 'hometown' or 'favorite food'.")
                    else:
                        print("Invalid index! Please enter a number within the range.")
                else:
                    print("Invalid input! Please enter a valid number.")
        elif action == 'quit':
            print("Goodbye!")
            break
        else:
            print("Invalid action! Please enter 'add', 'view', or 'quit'.")

main()