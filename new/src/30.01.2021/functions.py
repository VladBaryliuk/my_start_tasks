def equate(number1, number2):
    resalt = (number1+4*number2)*(number1-3*number2)+number1
    return resalt
print(equate(5, 3))
def find_speed(kilometers, hours):
    resalt2 = kilometers / hours
    return resalt2
print(find_speed(100, 3))
def smallest(number1, number2, number3):
    if number1 < number2 and number1 <number3:
        return number1
    if number2 < number1 and number1 <number3:
        return number2
    if number3 < number2 and number1 <number1:
        return number3
print(smallest(3,1000,5))