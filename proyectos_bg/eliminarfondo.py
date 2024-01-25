from rembg import remove
from PIL import Image

quitar_fondo = remove(Image.open("omargripo.jpg")) # solo poner la imagen q luego quitaremos el fondo
quitar_fondo.save("perfil-omar-vg-hacking.png")

    