#!/usr/bin/python
# -*- coding: utf-8 -*-

# Marina Martín Hernández
# Ejercicio 14.5 - Sumador Simple:

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #!!
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #!!
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

first_time = True

try:
	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept() #!!
		print 'Request received:'
		URL          = recvSocket.recv(1024)      #Tomamos la URL
		data_list    = URL.split( )			      #La troceamos y la guardamos en una lista
		addend       = data_list[1][1:]	          #Tomamos únicamente el número
		print 'Answering back...'
		if first_time:
			first_addend = addend
			recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body bgcolor='#6CD0C8'><center><h1>" + 
							"<FONT FACE='courier'>" + "Your first number introduced: " + 
							str(first_addend) + "</p>" + "Introduce another one" + 
							"</FONT></body></html>\r\n")
			first_time = False
		else:
			last_addend = addend
			addition    = int(first_addend) + int(last_addend)
			print str(addition)
			recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
							"<html><body bgcolor='#B17FC9'><center><h1>" + 
							"<FONT FACE='courier'><font color='#FAF4F4'>" + 
							"First addend + Second addend = " + "</p>" + 
							str(first_addend) + "   +   " + str(last_addend) + " =" +
							"</p>" + str(addition) + "</font></FONT></body></html>\r\n")
			first_time = True
	recvSocket.close()
except KeyboardInterrupt:
    print "Closing binded socket"
    mySocket.close()
