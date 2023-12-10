from PIL import Image
def ocultar_datos(imagen_original, datos_a_ocultar, imagen_salida):
    # Abre la imagen original
    img = Image.open(imagen_original)
    # Convierte los datos a binario
    datos_binarios = ''.join(format(ord(char), '08b') for char in datos_a_ocultar)
    datos_index = 0
    # Itera sobre cada píxel de la imagen
    for i in range(img.width):
        for j in range(img.height):
            pixel = list(img.getpixel((i, j)))
            # Modifica el bit menos significativo de cada componente de color
            for c in range(3):  # R, G, B
                if datos_index < len(datos_binarios):
                    pixel[c] = pixel[c] & ~1 | int(datos_binarios[datos_index])
                    datos_index += 1
            img.putpixel((i, j), tuple(pixel))
    # Guarda la imagen modificada
    img.save(imagen_salida)
# Ejemplo de uso
imagen_original = "avengers.jpg"
datos_a_ocultar = "Gaa Caiste Ten en cuenta donde das click hacking in python"
imagen_salida = "hack_set.png"
ocultar_datos(imagen_original, datos_a_ocultar, imagen_salida)
