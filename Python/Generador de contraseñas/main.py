from zxcvbn import zxcvbn
import random as rd
import string
import asyncio

vocabulario = [c for c in (string.ascii_letters + string.digits + string.punctuation)]
longitudPassword = 16
catalogoSeguridad = {
    0: "Débil",
    1: "Insuficiente",
    2: "Normal",
    3: "Bueno",
    4: "Máximo"
}

async def confirmacionProceso():
    entrada = str(input("\tPulse cualquier tecla para iniciar el proceso de generación de contraseña"))
    if(entrada != None):
        print("\n\tLa contraseña se está generando (este proceso puede llevar unos minutos u horas)")
        password, puntuacion, estimacionFiltrado = await generarPassword(vocabulario)
    imprimirResultados(password, estimacionFiltrado)

async def generarPassword(vocabulario):
    puntuacionObtenida = 0
    passwordGenerada = ""

    while puntuacionObtenida != 4: # si la seguridad de la contraseña generada no es la máxima -> volver a generar una nueva contraseña

        for i in range(longitudPassword):
            passwordGenerada += vocabulario[rd.randint(0, len(vocabulario)-1)]

        try:
            puntuacionObtenida = zxcvbn(passwordGenerada)["score"]
        except IndexError: # Si ocurre un error (por ejemplo, en contraseñas muy simples)
            continue

    tiempoEstimadoParaSuFiltrado = zxcvbn(passwordGenerada)["crack_times_display"]["offline_slow_hashing_1e4_per_second"] # El tiempo estimado para adivinar la password generada
    return passwordGenerada, catalogoSeguridad[puntuacionObtenida], tiempoEstimadoParaSuFiltrado

def imprimirResultados(password, estimacionFiltrado):
    print("\t==============================================================")
    print("\tContraseña generada:", password)
    print("\tTiempo estimado para que logren adivinar la contraseña:", estimacionFiltrado)
    print("\t==============================================================\n")

def imprimirPresentacion():
    print("\t==============================================================")
    print("\tGenerador de contraseñas seguras")
    print("\tAutor: Miguel Fernández Huerta")
    print("\t==============================================================")

def main():
    imprimirPresentacion()
    asyncio.run(confirmacionProceso())

main()

