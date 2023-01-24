import os

class OperasBas:
    #declaracion de variables
    num1=0
    num2=0
    res=0

    #declaracion de constructor
    def __init__(self):
        self.num1=3
        self.num2=4
        self.res=0

    def suma(self):
        num1=int(input("Dame num1: "))
        num2=int(input("Dame num2: "))
        self.res=num1+num2
        print("La suma es: {}".format(self.res))
    
    def resta(self):
        num1=int(input("Dame num1: "))
        num2=int(input("Dame num2: "))
        self.res=num1-num2
        print("La resta es: {}".format(self.res))
    
    def multiplicacion(self):
        num1=int(input("Dame num1: "))
        num2=int(input("Dame num2: "))
        self.res=num1*num2
        print("La multiplicacion es: {}".format(self.res))
    
    def division(self):
        num1=int(input("Dame num1: "))
        num2=int(input("Dame num2: "))
        self.res=num1/num2
        print("La division es: {}".format(self.res))

def main():
        obj=OperasBas()
        num3=0
        while num3!=5:
            print("Menu \n1.-Suma\n2.-Resta\n3.-Multiplicacion\n4.-Division\n5.-Salir")
            num3=int(input("Operacion a realizar: "))
            if num3 ==1:
                obj.suma()
            if num3 ==2:
                obj.resta()
            if num3 ==3:
                obj.multiplicacion()
            if num3 ==4:
                obj.division()
            if num3 ==5:
                print("Saliendo de la aplicacion")
                os.system('cls')
            if num3 >5:
                print("Error de operacion")

    #declaracion de metodos de clase
if __name__ == "__main__":
        main()