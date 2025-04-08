def calcular_pulsaciones(edad):
    pulsaciones = (220 - edad) / 10
    return pulsaciones


edad = int(input("Ingresa tu edad: "))

pulsaciones = calcular_pulsaciones(edad)

print(f"\nNúmero de pulsaciones por cada 10 segundos de ejercicio: {pulsaciones:.1f}")
