import socket

SERVER=socket.gethostbyname(socket.gethostname())
PORT=12345
ADDRESS =(SERVER,PORT)
FORMAT="utf-8"
BTYESIZE=1024
DISCONNECT_MESSAGE="quit"


client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDRESS)

while True:
    message=client.recv(BTYESIZE).decode(FORMAT)

    if message == DISCONNECT_MESSAGE:
        client.send("quit".encode(FORMAT))
        print("çıkış yapılıyor....")
        break
    else:
        print(f"{message}\n")
        message=input("mesaj..:")
        client.send(message.encode(FORMAT))
client.close()