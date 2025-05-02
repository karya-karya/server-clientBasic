from socket import *
serverName = "localhost"
serverPort= 15000
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))
sentence = input("input: ")
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(2048).decode()
print("AFTER SENDING SERVER:", modifiedSentence)

clientSocket.close()
