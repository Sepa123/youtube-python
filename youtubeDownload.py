from pytube import YouTube

try:
    ytUrl = input("ingrese una URL de un video de YouTube: ")
    ytVideo = YouTube(ytUrl)

    print("Descargando Video ...")

    video = ytVideo.streams.get_by_resolution("720p") 
    # ytVideo.streams.get_highest_resolution() # para obtener la max resolucion posible
    video.download()
  
    print("video descargado ...")

except:
    print("Error con la Url ingresada")


