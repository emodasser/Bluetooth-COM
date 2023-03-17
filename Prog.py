import bluetooth

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
client_socket,addr = server_socket.accept()
print("Accepted connection from ",addr)
print ("Envoyez 'exit' depuis le téléphone pour quitter")

while True:
    messageRecu = ""
    while True:
        res = client_socket.recv(1024)
        client_socket.send(res)
        if res[0] == 0x0D:
            print("")
            break
        else:
            messageRecu = messageRecu + res.decode();
    
    if messageRecu == "exit":
        print ("Vous avez quitter le programme")
        break
    else:
        print("Received:",messageRecu)
        print("Ecrivez un message")
        msg=input()
        client_socket.send(msg)
        

client_socket.close()
server_socket.close()
