# producto alg1 1.-Compra de artículos,
# Si los artículos comprados son menores a 3 Pagar en efectivo,
# caso contrario pagar con tarjeta.

Compras_Pagar = int(input(" ? cuantos articulos compraste ?: "))
if Compras_Pagar <3:
    print("debes pagar en efectivo")
else:
    print("debes pagar con tarjeta")