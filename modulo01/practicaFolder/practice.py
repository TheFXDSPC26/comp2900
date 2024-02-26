weightEnter = float(input('Enter Weight: '))

print(weightEnter)

convEnter = input('Would you like to convert the typed weight to lbs or kg?\n\nC=yes\nAny other key=no\n\n')
convEnter = convEnter.upper()

if convEnter == 'C':
    uConv = input('Type K to convert to kilograms or L for pounds: ')
    uConv = uConv.upper()

    if uConv == 'K':
        weightEnter = weightEnter * 0.453592
        print(f'Weight in KG is {weightEnter} kg')
        exit()
    elif uConv == 'L':
        weightEnter = weightEnter * 2.20462
        print(f'Weight in Lbs is {weightEnter} lbs')
        exit()
    else:
        print('Invalid option selected')

else:
   optSelec = input('Is the typed weight in Lbs(L) or Kg(K)? ')
   optSelec = optSelec.upper()

if optSelec == 'K':
        print(f'Weight in KG is {weightEnter} kg')
elif optSelec == 'L':
        print(f'Weight in Lbs is {weightEnter} lbs')
else:
        print('Invalid option selected')