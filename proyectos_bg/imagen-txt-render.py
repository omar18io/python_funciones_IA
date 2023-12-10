import pywhatkit

pywhatkit.image_to_ascii_art("dibujo.png", "archivo-render-ga")

leer_archivo = open("archivo-render-ga.txt")
print(leer_archivo.read())
