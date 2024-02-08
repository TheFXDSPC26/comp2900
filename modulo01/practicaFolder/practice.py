num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator sign to choose math operation: ")

while (operator != 'e'):

    if (operator == '+'):
        print(f'Sum is {num1+num2}')
    elif (operator == '-'):
        print(f'Difference is {num1-num2}')
    elif (operator == '*'):
        print(f'Product is {num1*num2}')
    elif (operator == '/'):
        print(f'Division is {num1/num2}')
    else :
        print('Invalid operator')
        operator = input("Enter operator sign to choose math operation: ")

    