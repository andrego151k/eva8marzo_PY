# si trabaja mas de 40 horas 50% mas de las horas extras
horas = int(input("Ingrese las horas trabajadas: "))

valor_h = 5000
valor_hext = 7500

if horas <= 40:
    print(horas * valor_h)

else:
    print(horas * valor_h +
          (horas - 40) * valor_hext)