import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('sumador.edu', 8080))
mySocket.listen(5)
primero = True

try:

    while True:
        print ('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print ('HTTP request received:')
        URL = recvSocket.recv(1024)
        numero = URL.split()[1][1:]
        print 'Answering'
        if primero == True:
            numero1 = int(numero)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>" + "Primer sumando: " + str(numero1) +
                        "</p>" + "Dame otro" +
                        "</body></html>" + "\r\n")
            primero = False
        else:
            resultado = numero1 + int(numero)
            recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>" + "Primer sumando: " + str(numero1) +
                        "</p>" + "Segundo sumando: " + str(numero) +
                        "</p>" + "El resultado es: " + str(resultado) +
                        "</body></html>" + "\r\n")
            primero = True
        recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
