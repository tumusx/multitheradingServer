import socket
from threading import Thread

server_IP = "127.0.0.1"
server_port = 20004
buffer_size = 1024


def task(client_socket):
    message = client_socket.recv(buffer_size).decode('utf-8')

    splitReivecdClient = message.split(' ')
    requestingFile = splitReivecdClient[1]

    fileClientRequesting = requestingFile.split('?')[0]
    fileClientRequesting = fileClientRequesting.lstrip('/')

    print("arquivo que o cliente requisitou " + requestingFile)

    try:
        reply_msg = 'HTTP/1.0 200ok\n'
        fileClient = open(fileClientRequesting, 'rb')
        responseFile = fileClient.read()
        fileClient.close()
        if fileClientRequesting.endswith('.png'):
            mimetypes = 'image/png'
        else:
            mimetypes = 'text/html'

        reply_msg += 'Content-type: ' + str(mimetypes) + '\n\n'
        final_Response = reply_msg.encode('utf-8')
        final_Response += responseFile
        client_socket.send(final_Response)
        client_socket.close()
        print("arquivo existente")

    except Exception as e:
        reply_msg = 'HTTP/1.1 404 Not Found\n\n'
        print("O cliente requisitou o arquivo errado")

    reply_msg.encode('utf-8')
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
