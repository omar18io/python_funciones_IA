import os
import requests
import urllib.parse  # Para manejar la URL y extraer el nombre del archivo

def descargar_archivo(url_archivo):
    try:
        # Realiza una solicitud GET a la URL del archivo
        response = requests.get(url_archivo)
        
        # Verifica si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Obtiene el nombre del archivo desde la URL
            nombre_archivo = os.path.basename(urllib.parse.urlparse(url_archivo).path)
            
            # Elimina caracteres no permitidos del nombre del archivo
            nombre_archivo = "".join(c for c in nombre_archivo if c.isalnum() or c in ('.', '_'))
            
            # Guarda el contenido de la respuesta en el archivo en el directorio actual
            ruta_destino = os.path.join(os.getcwd(), nombre_archivo)
            
            with open(ruta_destino, 'wb') as file:
                file.write(response.content)
            print(f"Descarga exitosa. Archivo guardado en: {ruta_destino}")
        else:
            print(f"Error al descargar: Código de estado {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# URL del archivo a descargar
url = "https://img.freepik.com/psd-premium/banner-publicacion-redes-sociales-fiesta-noche-halloween-o-plantilla-publicacion-instagram_612040-1452.jpg?w=2000"

# Llama a la función descargar_archivo con la URL
descargar_archivo(url)
