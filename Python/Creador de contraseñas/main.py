import random as rd

passwordGenerada = ""
vocabulario = ''.join(chr(i) for i in range(0x110000) if chr(i).isprintable())

longitud = None

while longitud == None:
    try:
        longitud = int(input("Ingresa la longitud que quieras que tenga la contraseña: "))
    except ValueError as e:
        print("Tienes que ingresar un valor numérico para la longitud de la cadena")

for i in range(longitud):
    index = rd.randint()
    print(index, "\n")

