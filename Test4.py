#Escribir un programa para verificar si un número es primo o no. 



def esPrimo(num):
    if (num < 1):
        return False
    else:
        if (num % 2 == 0):
            return True
        else: 
            return False

num = int(input("Escriba un número: "))
resultado = esPrimo(num)

