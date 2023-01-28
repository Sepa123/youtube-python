Scripts de python para descargar videos de YouTube;
y obtener el texto de un video de youtube en formato .pdf


## Requerimientos

- Python 3.10
- [PyTube](https://pytube.io/en/latest/index.html)
- [Whisper](https://github.com/openai/whisper) + ffmpeg
- [fpdf](https://pyfpdf.readthedocs.io/en/latest/)

Para instalar ffmpeg, segun el sistema operativo se instala de la siguiente forma

```bash
# Ubuntu
sudo apt update && sudo apt install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg

#  MacOS con Homebrew (https://brew.sh/)
brew install ffmpeg

# Windows con Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# Windows con Scoop (https://scoop.sh/)
scoop install ffmpeg
```

## Como usar los scripts

Si deseas descargar un video de youtube, deberas ejecutar youtubeDownload.py e ingresar el Url del video.

```bash
python youtubeDownload.py 

ingrese una URL de un video de YouTube: https://www.youtube.com/watch?v=lc5JJTQa4r8

```
En cambio, si desea descargar el .pdf con el texto del video de youtube, debera ejecutar youtubeText.py




