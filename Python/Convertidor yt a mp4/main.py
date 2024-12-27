from pytube import YouTube

def descargar_video(url, ruta_descarga):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution().download(ruta_descarga)
        print("¡Descarga completada!")
    except Exception as e:
        print("Ocurrió un error:", str(e))

url = input("Introduce la URL del video de YouTube: ")
ruta_descarga = 'D:\TRABAJOS\Desktop'
descargar_video(url, ruta_descarga)

# hacer en el escritorio una carpeta llamada 'Descargas'