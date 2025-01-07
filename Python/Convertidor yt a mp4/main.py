from pytube import YouTube

"""ATENCIÓN: ESTE CÓDIGO YA NO FUNCIONA DEBIDO A QUE YOUTUBE HA CAMBIADO LA FORMA DE REALIZAR LAS PETICIONES IMPIDIENDO EL ACCESO Y DESCARGA DEL VÍDEO"""

def mensajeProgreso():
    print("Accediendo al contenido del vídeo...")

def descargar_video(url):
    try:
        yt = YouTube(url, on_progress_callback=mensajeProgreso())
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        print("¡Descarga completada!")
    except Exception as e:
        print("Ocurrió un error:", str(e))

def solicitarURL():
    url = None
    while url == None:
        url = input("Introduce la URL del video de YouTube: ")
    return url

def imprimirPresentacion():
    print("\t==============================================================")
    print("\tConvertidor de vídeos de Youtube a mp4")
    print("\tAutor: Miguel Fernández Huerta")
    print("\t==============================================================")

def main():
    imprimirPresentacion()
    descargar_video(solicitarURL())

main()