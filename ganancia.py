def calcular_precio_venta(precio_compra, porcentaje_ganancia=30):
    precio_venta = precio_compra * (1 + porcentaje_ganancia / 100)
    return precio_venta


precio_compra = float(input("Ingresa el precio de compra del artículo: "))


precio_venta = calcular_precio_venta(precio_compra)


print(f"\nEl precio de venta con una ganancia del 30% es: C${precio_venta:.2f}")
