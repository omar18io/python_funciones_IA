import time
from plyer import notification

def obtener_input_usuario():
    """Obtiene el título y el mensaje del usuario."""
    title = input("Ingrese el título de la notificación: ")
    message = input("Ingrese el mensaje de la notificación: ")
    return title, message

def mostrar_notificacion(title, message, timeout=10):
    """Muestra una notificación con el título y el mensaje especificados."""
    notification.notify(title=title, message=message, timeout=timeout)
    
def programar_notificaciones():
    """Programa notificaciones para ser mostradas en intervalos."""
    title, message = obtener_input_usuario()
    for _ in range(3):  # Mostrar 3 notificaciones en intervalos de 10 segundos
        mostrar_notificacion(title, message)
        time.sleep(10)
        
if __name__ == "__main__":
    programar_notificaciones()
