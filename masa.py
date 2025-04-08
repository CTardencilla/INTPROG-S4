def calcular_masa(presion, volumen, temperatura):
    masa = (presion * volumen) / (0.37 * (temperatura + 460))
    return masa


presion = float(input("Ingresa la presión: "))
volumen = float(input("Ingresa el volumen: "))
temperatura = float(input("Ingresa la temperatura (en °F): "))


masa = calcular_masa(presion, volumen, temperatura)


print(f"\nLa masa calculada es: {masa:.2f}")
