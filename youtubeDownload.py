import pytube

ytUrl = input("ingrese una URL de un video de YouTube: ")

ytVideo = pytube.YouTube(ytUrl)
print("Descargando Video ...")
video = ytVideo.streams.get_by_resolution("720p") 
# ytVideo.streams.get_highest_resolution() # para obtener la max resolucion posible

video.download()

print("video descargado ...")

