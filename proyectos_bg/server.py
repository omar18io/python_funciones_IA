import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode("utf-8")
            print(f"Mensaje recibido: {message}")

            # Respuesta al cliente
            response = f"Servidor: Recibí tu mensaje: {message}"
            client_socket.send(response.encode("utf-8"))
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            break

    client_socket.close()

def start_server():
    server_address = ("localhost", 5500)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print(f"Servidor escuchando en {server_address}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Conexión aceptada desde {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
