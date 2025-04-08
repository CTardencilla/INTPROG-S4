cantidad_mujeres = int(input("Ingrese la cantidad de mujeres: "))
cantidad_varones = int(input("Ingrese la cantidad de varones: "))

total_estudiantes = cantidad_mujeres + cantidad_varones

if total_estudiantes == 0:
    print("No hay estudiantes en el aula.")
else:
    
    porcentaje_mujeres = (cantidad_mujeres / total_estudiantes) * 100
    porcentaje_varones = (cantidad_varones / total_estudiantes) * 100

   
    print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
    print(f"Porcentaje de varones: {porcentaje_varones:.2f}%")
