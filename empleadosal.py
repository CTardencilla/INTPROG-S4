
salario_actual = float(input("Ingrese el salario actual del empleado: "))

incremento = salario_actual * 0.08
salario_con_incremento = salario_actual + incremento


descuento = salario_con_incremento * 0.025
salario_final = salario_con_incremento - descuento


print(f"Salario con incremento: {salario_con_incremento:.2f}")
print(f"Descuento por servicios: {descuento:.2f}")
print(f"Salario final: {salario_final:.2f}")
