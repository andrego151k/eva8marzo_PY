print("poner 3 numeros cual es menor y la suma de los 3.")
Numero1= int(input("ingrese primer numero: "))
Numero2= int(input("ingrese el segundo: "))
Numero3= int(input("ingrese el tercero: "))

# el menor # la suma
if Numero1 < Numero2 and Numero1 < Numero3:
    print(f"El {Numero1} es el menor")
elif Numero2 < Numero1 and Numero2 < Numero3:
    print(f"El {Numero2} es el menor")
elif Numero3 < Numero1 and Numero3 < Numero2:
    print(f"El {Numero3} es el menor")

print(Numero1+Numero2+Numero3)