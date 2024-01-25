import cv2

def convertir_a_dibujo(imagen_path, nombre_salida='omar-hack-vgEd.png'):
    # Cargar la imagen
    imagen = cv2.imread(imagen_path)
    # Convertir la imagen a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    # Aplicar un desenfoque para suavizar la imagen
    suavizado = cv2.GaussianBlur(gris, (21, 21), sigmaX=0, sigmaY=0)
    # Detectar bordes con el operador Laplaciano
    bordes = cv2.Laplacian(suavizado, cv2.CV_8U, ksize=5)
    # Invertir la imagen para resaltar los bordes
    bordes = cv2.bitwise_not(bordes)
    # Guardar la imagen resultante
    cv2.imwrite(nombre_salida, bordes)
if __name__ == "__main__":
    # Ruta de la imagen de entrada
    imagen_path = 'omargripo.jpg'
    # Llamar a la función para convertir a dibujo
    convertir_a_dibujo(imagen_path)
    print("La conversión a dibujo ha sido completada. El dibujo se ha guardado como 'dibujo.png'")