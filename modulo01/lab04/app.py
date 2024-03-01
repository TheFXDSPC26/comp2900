import array

aNumber = array.array('i')

for i in range(0,4):
    inNum = int(input('Enter number: '))
    aNumber.append(inNum)
    
for i in range(4):
        print(f'Indice {i} - Valor {aNumber[i]}')

for n in aNumber:
      print(f'Valor {n}')

for i in range(len(aNumber)):
      print(f'Valor {i}')