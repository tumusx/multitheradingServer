import socket
from threading import Thread

server_IP = "127.0.0.1"
server_port = 20003
buffer_size = 1024


def task(client_socket):
    message = client_socket.recv(buffer_size)
    tipo_arquivo = 'text/html'
    reply_msg = 'HTTP/1.0 200ok/n'
    reply_msg = reply_msg + 'Content-type: {}\r\n\r\n'.format(tipo_arquivo)
    reply_msg = reply_msg + '<html><body>SISTEMAS DISTRIBUIDOS -> PARTE 1</body></html>'
    bytes_to_send = str.encode(reply_msg)
    client_socket.send(bytes_to_send)
    print(message)


# cria o socket tcp
tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# define a porta
tcp_server_socket.bind((server_IP, server_port))
print("servidor web funcionando e esperando conexoes")

# espera o recebimento
while (True):
    tcp_server_socket.listen()

    client_socket, address = tcp_server_socket.accept()

    t = Thread(target=task, args=(client_socket,))
    t.start()
