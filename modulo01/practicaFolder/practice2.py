import array

arr = array.array('d')

x = int(input('How many numbers would you like to store in the main array?: '))

for i in range(x):
     numVal = float(input('Type any number: '))
     arr.append(numVal)

for y in range(x):
       print(f'Position {y} = {arr[y]}') 

for i in range(len(arr)):
      print(arr[i])
