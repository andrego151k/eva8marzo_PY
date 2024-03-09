Horas = int(input("ingrese total de horas trabajadas: "))
Horasext = int(input("ingrese horas extras trabajadas: "))
Valor_hora = 10
Valor_hextra = 5

if Horas <= 40:
        pagohoras = Valor_hora * Horas
        print (pagohoras)
elif Horas > 40:
            pagoextras = (Valor_hora * Horas) + (Horasext * Valor_hextra)
            print (pagoextras)