import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

class ChatGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat en Red")

        self.chat_history = scrolledtext.ScrolledText(master, width=40, height=10)
        self.chat_history.pack(pady=10)

        self.message_entry = tk.Entry(master, width=40)
        self.message_entry.pack(pady=10)

        self.send_button = tk.Button(master, text="Enviar", command=self.send_message)
        self.send_button.pack()

        self.server_address = ("localhost", 5500)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_address)

        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.client_socket.send(message.encode("utf-8"))
            self.message_entry.delete(0, "end")

    def receive_messages(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                message = data.decode("utf-8")
                self.chat_history.insert("end", f"{message}\n")
                self.chat_history.yview("end")
            except Exception as e:
                print(f"Error al recibir mensaje: {e}")
                break

if __name__ == "__main__":
    root = tk.Tk()
    chat_app = ChatGUI(root)
    root.mainloop()
