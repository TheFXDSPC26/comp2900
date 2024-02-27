

def age(curYear, birYear):
    global currentYear
    global birthYear
    currentAge = curYear - birYear
    print(f'Your age is{currentAge}')

currentYear = float(input('Current Year: '))
birthYear = float(input('Current Year: '))

printYear = age(currentYear, birthYear)

print(f'{printYear}')