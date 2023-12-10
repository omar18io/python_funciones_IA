from rembg import remove
from PIL import Image

quitar_fondo = remove(Image.open("omargripo.jpg"))
quitar_fondo.save("perfil-omar-vg-hacking.png")

    