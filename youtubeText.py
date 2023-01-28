from pytube import YouTube
import whisper
from fpdf import FPDF
import os

try:
    ## Descarga el audio de un video de YouTube

    ytUrl = input("ingrese una URL de un video de YouTube: ")

    ytVideo = YouTube(ytUrl)
    titleAudio = ytVideo.title.replace(" ","_")

    audio = ytVideo.streams.get_audio_only()
    print("Descargando Audio ...")
    audio.download(filename=titleAudio + ".mp4")

    #Transcribiendo con Whisper

    model = whisper.load_model("small")
    print("Trascribiendo ...")
    result = model.transcribe(titleAudio + ".mp4", fp16=False)

    print("Transcripción completada")

    #Convertir a pdf 

    print("Escribiendo el texto de audio en formato .pdf")

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Arial", size = 14)
    pdf.cell(200,10,txt = ytVideo.title, align= "C")
    pdf.ln()
    pdf.set_font("Arial", size = 12)
    pdf.multi_cell(0,5,txt = result["text"], border = 0, align= "J")

    pdf.output(titleAudio +".pdf")

    # eliminando audio descargado

    os.remove(titleAudio + ".mp4")
except:
    print("Error con la Url ingresada")