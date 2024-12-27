from zxcvbn import zxcvbn
import random as rd
import string

catalogoSeguridad = {
    0: "Débil",
    1: "Insuficiente",
    2: "Normal",
    3: "Bueno",
    4: "Máximo"
}

def solicitarLongitud():
    longitud = None
    
    while longitud == None:
        try:
            
            longitud = int(input("Ingresa la longitud que quieras que tenga la contraseña: "))
        except ValueError as e:
            print("Tienes que ingresar un valor numérico para la longitud de la cadena")

    return longitud
    
def generarPassword(longitud, vocabulario):
    puntuacionObtenida = 0

    while puntuacionObtenida < 3: # si la seguridad de la contraseña generada no es la deseada -> volver a generar una nueva contraseña
        passwordGenerada = ""

        for i in range(longitud):
            passwordGenerada += vocabulario[rd.randint(0, len(vocabulario)-1)]

        try:
            puntuacionObtenida = zxcvbn(passwordGenerada)["score"]
        except IndexError: # Si ocurre un error (por ejemplo, en contraseñas muy simples)
            continue

    tiempoEstimadoParaSuFiltrado = zxcvbn(passwordGenerada)["crack_times_display"]["offline_slow_hashing_1e4_per_second"] # El tiempo estimado para adivinar la password generada
    return passwordGenerada, catalogoSeguridad[puntuacionObtenida], tiempoEstimadoParaSuFiltrado



def main():
    vocabulario = [c for c in (string.ascii_letters + string.digits + string.punctuation)]

    password, puntuacion, estimacionFiltrado = generarPassword(solicitarLongitud(), vocabulario)

    print("\n\t==============================================================")
    print("\tContraseña generada:", password)
    print("\tNivel de seguridad logrado", puntuacion)
    print("\tTiempo estimado para que logren adivinar la contraseña:", estimacionFiltrado)
    print("\t==============================================================\n")

main()

