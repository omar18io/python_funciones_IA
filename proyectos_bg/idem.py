from idm import IDMan
def descargar_archivo(url_archivo, ruta_destino):
    # Inicia una instancia de la clase IDMan
    downloader = IDMan()

    # Descarga el archivo desde la URL proporcionada
    # Utiliza la ruta de descarga especificada como destino
    downloader.download(url_archivo, ruta_destino)
# URL del archivo a descargar
url = "https://img.freepik.com/psd-premium/banner-publicacion-redes-sociales-fiesta-noche-halloween-o-plantilla-publicacion-instagram_612040-1452.jpg?w=2000"

# Ruta completa de destino para la descarga
ruta_destino = "C:\\Users\\Usuario\\Desktop\\img_descarga"

# Llama a la función descargar_archivo con la URL y la ruta de destino
descargar_archivo(url, ruta_destino)


