
import socket as sk
from socket import *
import os

files = [file for file in os.listdir('.') if os.path.isfile(file)]
serverName = '127.0.0.1'
serverPort = 12010
clientSocket = socket(AF_INET, SOCK_STREAM) #creates client socket param1: network using IPv4. param2: TCP socket
clientSocket.connect((serverName, serverPort)) #initiates TCP connection between client and server
sentence = input('Input lowercase sentence:') #obtains sentence from user
clientSocket.send(sentence.encode()) #sends the sentence through the client's socket into the TCP #connection
#client waits to recive bytes from the server
modifiedSentence = clientSocket.recv(1024) #when characters arrive from server, they become #modifiedSentence 
print('New Sentence From Server: ', modifiedSentence.decode(), '\nServer Machine:', sk.gethostname(), '\nFiles @ Current Location:', files) #print capitalized sentence
clientSocket.close() #close socket and TCP connection, client TCP sends TCP message to server TCP

