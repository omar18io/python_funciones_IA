import socket
import threading
def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"Cliente {address}: {message}")
            
            # Reenviar el mensaje a todos los clientes conectados
            broadcast(message, client_socket)
        except Exception as e:
            print(f"Error: {e}")
            break

    # Eliminar el cliente cuando se desconecta
    remove_client(client_socket)
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error al enviar mensaje: {e}")
                remove_client(client)

def remove_client(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Configuración del servidor
host = "127.0.0.1"
port = 5555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Servidor escuchando en {host}:{port}")

clients = []

# Manejar conexiones de clientes
while True:
    client, address = server.accept()
    print(f"Conexión aceptada desde {address}")
    clients.append(client)

    # Iniciar un hilo para manejar al cliente
    client_thread = threading.Thread(target=handle_client, args=(client, address))
    client_thread.start()
