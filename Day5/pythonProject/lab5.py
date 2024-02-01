def apt_search1(city, max_rent, min_beds, pets_allowed):
    max_rent = int(max_rent)
    min_beds = int(min_beds)
    if pets_allowed == True:
        print(f'''
        Welcome to GC Property Management! Looking up listings in\n
         {city} for {min_beds} bedroom apartments that allow pets, all within a\n
         budget of {max_rent} per month...''')
    else:
        print(f'''
        Welcome to GC Property Management! Looking up listings in\n
        {city} for {min_beds} bedroom apartments, all within a\n
        budget of {max_rent} per month... ''')

#apt_search1('Rock hill', 3000, 3, False )

def apt_search2(city, max_rent, min_beds = 'any amount of', pets_allowed = ''):

    if pets_allowed == True:
        print(f'''
           Welcome to GC Property Management! Looking up listings in\n
            {city} for {min_beds} bedroom apartments that allow pets, all within a\n
            budget of {max_rent} per month...''')
    else:
        print(f'''
           Welcome to GC Property Management! Looking up listings in\n
           {city} for {min_beds} bedroom apartments, all within a\n
           budget of {max_rent} per month... ''')

apt_search2('Rock Hill', 3000, 3, True )


plus_100 = lambda var1: var1 + 100
print(plus_100(100))
squared = lambda var2: var2 ** 2
print(squared(10))
concat = lambda var3: '-' + var3
print(concat('Hello'))
divide = lambda var4: var4 / 3
print(divide(9))