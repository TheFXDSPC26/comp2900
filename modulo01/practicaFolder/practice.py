enterWeight = float(input('Enter weight (in pounds): '))


weight = enterWeight

enterUnit = input('Would you like the information shown in (k)kg or (l)lb: ')

if (enterUnit  == 'l'):
    print(f'{weight:.2f}')
elif (enterUnit == 'k'):
    kg= weight * 0.453592
    print(f'{kg:.2f}')
else:
    print('Error')