
def calcular_salario(nombre, horas_trabajadas, precio_por_hora):
    
    sueldo_bruto = horas_trabajadas * precio_por_hora
    
    
    descuento_impuesto = sueldo_bruto * 0.05
    
    
    salario_neto = sueldo_bruto - descuento_impuesto
    
    # Imprimir los resultados
    print("\nResumen del salario:")
    print(f"Nombre del trabajador: {nombre}")
    print(f"Sueldo bruto: ${suel
