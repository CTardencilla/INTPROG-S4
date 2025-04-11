#Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su salario actual y un descuento de 2,5% por servicios.
salarioViejo = float(input("Dime el salario antiguo del empleado:"))
incremento = 8
descuento = 2.5
salarioNuevo = salarioViejo * (1 + incremento / 100)
salarioDesc = salarioNuevo * ( descuento / 100)
salarioFinal = salarioNuevo - salarioDesc
print("El salario nuevo del empleado tomando en cuenta el incremento del 8% y el descuento de servicios del 2.5% es de:",salarioFinal)

