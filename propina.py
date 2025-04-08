def calcular_propina(total_cuenta, porcentaje_propina):
    propina = total_cuenta * (porcentaje_propina / 100)
    return propina


total = float(input("Ingresa el total de la cuenta: "))
porcentaje = float(input("Ingresa el porcentaje de propina (por ejemplo, 10 para 10%): "))

propina = calcular_propina(total, porcentaje)
print(f"Debes dejar una propina de: ${propina:.2f}")
