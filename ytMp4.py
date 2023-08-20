from pytube import YouTube
from pytube.cli import on_progress

# try:
ytUrl = input("ingrese una URL de un video de YouTube: ")
ytVideo = YouTube(url=ytUrl )

print("Descargando audio ...")

video = ytVideo.streams.get_audio_only()
# ytVideo.streams.get_highest_resolution() # para obtener la max resolucion posible
video.download(output_path=r"C:\Users\sabo0\Desktop\BOB\mp4\Musica")

print("Audio descargado ...")

# except:
#     print("Error con la Url ingresada")