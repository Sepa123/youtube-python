from pytube import YouTube
from pytube.cli import on_progress

try:
    ytUrl = input("ingrese una URL de un video de YouTube: ")
    ytVideo = YouTube(url=ytUrl, on_progress_callback=on_progress)

    
    print("Descargando Video ...")

    video = ytVideo.streams.get_highest_resolution()
    # ytVideo.streams.get_highest_resolution() # para obtener la max resolucion posible
    print(f"tamaño: {round(video.filesize_mb,2)} Mb")
    
    video.download(output_path=r"C:\Users\sabo0\Desktop\BOB\mp4\Videos")


except:
    print("Error con la Url ingresada")