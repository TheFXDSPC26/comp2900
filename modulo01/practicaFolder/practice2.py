x = int(input('How many names would you like to store in the main array?: '))

strList = []

for i in range(x):
     nameVal = input('Type any name: ')
     strList.append(nameVal)

for y in range(x):
       print(f'Position {y} = {strList[y]}') 

for i in range(len(strList)):
      print(strList[i])