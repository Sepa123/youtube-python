import pytube

## Descarga el audio de un video de YouTube

ytUrl = input("ingrese una URL de un video de YouTube: ")

ytVideo = pytube.YouTube(ytUrl)
print("Descargando Video ...")
video = ytVideo.streams.get_by_resolution("720p") # para resolucion de 720p
# ytVideo.streams.get_highest_resolution() # para obtener la max resolucion posible

video.download()

print("video descargado ...")

# https://www.youtube.com/watch?v=_y9qQZXE24A&t=36sS
