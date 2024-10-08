#Escribir un programa para verificar si un número es primo o no. 

def esPrimo(num):
    if (num < 1):
        return False
    elif num==2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

num = int(input("Escriba un número: "))
resultado = esPrimo(num)

if resultado:
    print("El número introducido es primo")
else: 
    print("El número introducido NO es primo")
