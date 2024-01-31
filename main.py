actual_temp = int(input('What is the temp of your home? '))
desired_temp = int(input('What is the desired temp of your home? '))


def  heating_cooling(actual_temp, desired_temp):
    if actual_temp < desired_temp:
        print('Run Heat')
    elif actual_temp > desired_temp:
        print('Run A/C')
    else:
        print('Standby')
    return
temp = heating_cooling(actual_temp,desired_temp)


def convert_temp(temp_c, target_U_input):
    target_U_input = target_U_input.lower()
    if target_U_input == 'k':
        return (temp_c + 273.15)
    elif target_U_input =='f':
        return ((temp_c * 9/5) + 32)
    elif target_U_input == 'c':
        return (temp_c)



print(convert_temp(80, 'F'))
