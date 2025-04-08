
nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (%): "))


descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - descuento

print(f"\nProducto: {nombre_producto}")
print(f"Precio final con descuento: C${precio_final:.2f}")
