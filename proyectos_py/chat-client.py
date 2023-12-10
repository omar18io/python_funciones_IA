import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(data.decode("utf-8"))
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            break

# Configuración del cliente
host = "127.0.0.1"
port = 5555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Iniciar un hilo para recibir mensajes del servidor
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Enviar mensajes al servidor
while True:
    message = input()
    client.send(message.encode("utf-8"))
