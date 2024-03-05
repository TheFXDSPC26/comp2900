import array

aNumber = array.array('d')
Lista_numeros = 0   
x = int(input('How many numbers would you like to type?: '))
y=x

for i in range(x):
      numInput = float(input('Welcome to the average calculator! Type a number: '))
      aNumber.append(numInput)
      print(f'{aNumber[i]}')

for i in range(x):
        
        Lista_numeros+=aNumber[i]

def lista_numeros(Lista_numeros):
       return Lista_numeros/x

res = lista_numeros(Lista_numeros)
print(res)