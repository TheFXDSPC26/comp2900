from array import array

arr = array('l')

for i in range(10):
    arr.append(i)

array_string = arr.tobytes()
print(array_string)

arr2 = array('l')
arr2.frombytes(array_string)
print(arr2)