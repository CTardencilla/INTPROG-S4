import random


numero_secret = random.randint(1,10)
print(numero_secret)
num_user= int(input('Dime un numero del 1 al 10: '))

if numero_secret == num_user:
    print(f'Felicidades, adivinaste el numero: {numero_secret}')
else:
    print('sigue intentando')
