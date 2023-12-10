import os
import http.server
import socketserver

# Establece el directorio que quieres servir
directorio_a_servir = r"c:\Users\Usuario\Documents\CreacionPython"

# Configura el manejador SimpleHTTPRequestHandler
handler = http.server.SimpleHTTPRequestHandler

# Cambia al directorio especificado
os.chdir(directorio_a_servir)

# Inicia el servidor en el puerto 8000
with socketserver.TCPServer(("", 8000), handler) as httpd:
    print("Servidor en el puerto 8000...")
    # Sirve la aplicación hasta que se interrumpa con Ctrl+C
    httpd.serve_forever()
