

print("Validacion de numeros")

num1=int(input("Dame num1: "))
num2=int(input("Dame num2: "))

if num1 > num2:
    print("el {} es mayor que el {}".format(num1,num2))
else:
    print("el {1} es mayor que el {0}".format(num1,num2))

print("-------------Pedir una edad------------")

edad=int(input("Ingrese su edad: "))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("No eres mayor de edad")