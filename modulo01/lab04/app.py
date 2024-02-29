import array

arr = array.array('i')

for i in range(0,4):
    inNum = int(input('Enter number: '))
    arr.append(inNum)
    
for i in range(4):
        print(f'Indice {i} - Valor {arr[i]}')

for n in arr:
      print(f'Valor {n}')

for i in range(len(arr)):
      print(f'Valor {i}')