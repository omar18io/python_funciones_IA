import cv2

def leer_qr(ruta_qr):
    img = cv2.imread(ruta_qr)
    if img is not None:
        detector_qr = cv2.QRCodeDetector()
        data = detector_qr.detectAndDecode(img)
        return data[0] if data[0] else "No se encontraron códigos QR en la imagen."
    else:
        return "No se pudo cargar la imagen."

# Ejemplo de uso
ruta_imagen = "qrcode.68832886.png"
resultado = leer_qr(ruta_imagen)
print(resultado)
