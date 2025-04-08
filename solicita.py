def calcular_totales(precios, iva_porcentaje=15):
    subtotal = sum(precios)
    iva = subtotal * (iva_porcentaje / 100)
    total = subtotal + iva
    return subtotal, iva, total


precios = []
for i in range(1, 4):
    precio = float(input(f"Ingrese el precio del producto {i}: "))
    precios.append(precio)


subtotal, iva, total = calcular_totales(precios)


print(f"\nSubtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")
