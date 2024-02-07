name = ['Cole Jenkins', 'Sam Arwood', 'Fionna DaVinci', 'Rob Wood']
home_town = ['Rock Hill', 'Mobile', 'Los Angeles', 'Mexico City']
food = ['Sushi', 'Fried Chicken', 'Pizza', 'Tacos']


while True:
    display_list = input('Would you like to see a list of all of the students? (y or n)\n')
    if display_list.lower() == 'y':
        print(name)
    while True:
        try:
            selection = int(input('Which Student would you like to learn about (1-4)? '))
            if 1<=  selection < len(name) + 1:
                student_index = selection - 1
                student_name = name[student_index]


                print(f'Student {selection} is {student_name}')

                category = input('Would you like to know their Home town or Favorite Food? ')
                category = category.lower()
                if category.split() == 'home town' or 'favorite food':
                    if category == 'home town':
                        print(f'Student {selection}, {student_name}, home town is {home_town[student_index]}')
                    elif category == 'favorite food':
                        print(f'Student {selection}, {student_name}, favorite food is {food[student_index]}')
                    else:
                        print('This cateogry does not exist')
                else:
                    print('That is not a valid category')
            else:
                print('That is not a valid student number')

        except ValueError:
            print('That is not a proper value')
        another_student = input("Would you like to see another students info? (y/n)\n> ")
        if another_student.lower() != 'y':
            break
    break