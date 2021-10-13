from socket import *
import cv2
serverPort = 12010
serverSocket = socket(AF_INET, SOCK_STREAM) #create a TCP socket
serverSocket.bind(('', serverPort)) #associate serverPort with serverSocket
serverSocket.listen(1) #wait and listen for a client (max connections: 1)
print('The server is ready to receive')
capture = cv2.VideoCapture(0) #create capture object 
while True:
    connectionSocket, addr = serverSocket.accept() #when a client knocks, invoke accept() and create new socket in server connectionSocket
    #client and server complete handshake, creating TCP connection between clientSocket and connectionSocket
    #open camera & display camera window
    ret, frame = capture.read()
    cv2.imshow('Camera View', frame)
    sentence = connectionSocket.recv(1024).decode() #recieve string over connection
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())  #send bytes over connection
    #send the names of the files located in the current folder and the name of the server machine
capture.release() #take the picture
cv2.destroyAllWindows() #close the window
connectionSocket.close() #close connection socket. As long as serverSocket is open, another client can knock on the door and send a sentence