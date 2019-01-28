import socket
hostname = raw_input("Enter the Server IP address: ")
port = int(raw_input("Enter the port: "))

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Client socket Created\n")
clientSocket.connect((hostname, port))
print("Connection with server done")
HTMLfile = raw_input("Enter the filename with extension: ")
#clientSocket.send('GET /test.txt HTTP/1.0\n\n')
f = "/" + HTMLfile

data='GET '+ HTMLfile +' HTTP/1.0\r\n\r\n'
data=data.encode()
clientSocket.send(data)
print("Request sent to Server")
decdata = ""
while 1:
        recvmesg = clientSocket.recv(4096)
        decdata = decdata + recvmesg.decode()
        if not recvmesg:
                break

print("Data received!!")

#modifiedMessage.split('::')

data1 = decdata.split('\r\n\r\n')
print(data1[0]+'\n')
print(data1[1])
#modifiedSave = clientSocket.recv(4096)
file = open(HTMLfile,'wb')
#encodedData = dataArr[1].encode()

file.write(data1[1])
file.close()
clientSocket.close()
