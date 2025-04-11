#algoritmo que, dado el año de nacimiento de una persona y el año actual, calcule su edad actual y su edad en 10 años.

Año_nacimiento = int(input("Dime el año en que nacistes: "))
Año_actual = int(input("Dime el año actual: "))
Edad = Año_actual - Año_nacimiento
Edad_10 = Edad + 10

print("Tu edad actual es:",Edad,"años y tu edad en 10 años va a ser de:",Edad_10,"años")
