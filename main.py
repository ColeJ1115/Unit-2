random_text = input('Enter some text! ')
print(random_text)

try:
    random_number = int(input('Please enter a number. '))
    print(random_number + 1)
except ValueError:
    print('That is not a number')

random_float = float(input('Please enter a number with a decimal. '))
print(random_float + .5)

multiple_one = float(input('Please enter your first number to be multiplied. '))
multiple_two = float(input('Please enter the second number to be multiplied. '))
print(multiple_one * multiple_two)

multiple_a = float(input('Please enter your first number to be divided. '))
multiple_b = float(input('Please enter the second number to be divided. '))
print(multiple_a / multiple_b)


random_boo_value = (input('Enter a boolean value! (True or False) '))
random_boo_value2 = random_boo_value.lower()

if random_boo_value2 == 'true':
    random_boo_value = True
elif random_boo_value2 == 'false':
    random_boo_value = False
else:
    random_boo_value != True or False

if random_boo_value == True:
    print("You entered True!")
    print("The oppisite is false")
elif random_boo_value == False:
    print("You entered False!")
    print("The oppisite is true!")
else:
    print('There is no value')

# 1.7 alternate

#Ask user for value
user_input = input("Enter a boolean last time:")
#right = True if literally typed True since the comparrison is correct
#If not True typed then it is false
right = user_input == "True"
#This sets a boolean only value based off of if True matched what was typed
right2 = bool(right)
#Prints the results
print("You entered:", right2)
print("The opposite of what you entered is:", not right2)