
'''
Leer el numero 5

5x1=5
5X2=10
.
.
.
5X10=50
'''
print("Tabla de multiplicar")

num1=int(input("Dame un numero: "))

for num in range(1,11):
    print("{} x {} = {}".format(num1,num,(num1*num)))
    