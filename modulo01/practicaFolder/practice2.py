import array

arr = array.array('d')
 
for item in 'Python':
    print(item)

for i in arr:
     numVal = input('Type any number: ')
     arr[i] = arr.append(numVal)