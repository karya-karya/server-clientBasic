from socket import *
serverPort = 15000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("0.0.0.0", serverPort))
serverSocket.listen(5)
print("SERVER ", serverSocket.getsockname(), "IS READY")

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence =connectionSocket.recv(2048).decode()
    print(f"Received massage:{sentence}")
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
      