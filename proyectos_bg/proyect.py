import PIL.Image
import PIL.ImageDraw

# Carga la imagen
image = PIL.Image.open("hack_set.png")

# Crea un objeto ImageDraw para la imagen
draw = PIL.ImageDraw.Draw(image)

# Dibuja el Word Art sobre la imagen
draw.text((0, 0), "Hola mundo", (255, 0, 0))

# Guarda la imagen modificada
image.save("wordart.jpg")

