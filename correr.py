
def calcular_salario():
    
    nombre = input("Ingrese el nombre del trabajador: ")
    horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
    precio_por_hora = float(input("Ingrese el precio por hora: "))

    
    sueldo_bruto = horas_trabajadas * precio_por_hora

    
    descuento_renta = sueldo_bruto * 0.05

    
    salario_a_pagar = sueldo_bruto - descuento_renta

    
    print("\nResumen del salario:")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo bruto: {sueldo_bruto:.2f} unidades monetarias")
    print(f"Descuento de renta (5%): {descuento_renta:.2f} unidades monetarias")
    print(f"Salario a pagar: {salario_a_pagar:.2f} unidades monetarias")


calcular_salario()
