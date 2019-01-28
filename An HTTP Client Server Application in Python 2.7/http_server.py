import socket
import os
import sys

#For TCP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

hostname = raw_input("Enter the hostname: ")
port = raw_input("Enter the port number: ")

serverSocket.bind((hostname,int(port)))
serverSocket.listen(1)

print("The Server is ready :")

while True :

	connectionSocket, address = serverSocket.accept()
	msg = connectionSocket.recv(2048)

	decmsg = msg.decode()

	splitdecmsg = decmsg.split()
	print(splitdecmsg)

	if (splitdecmsg[0] == 'GET' ):
		#print("You're good to go!")
		try:#filename, extension = os.path.splitext(msg)
			f = splitdecmsg[1];
			fNew = f[1:];
			print "fNew: ", fNew;
			
			print("The file exists...")
		
			
			# break;



			obj = open(fNew,'rb')
			r = obj.read(2048)
			print("File read")


		#renc = r.encode()

		#Getting the size of the file
			sizeoffile = sys.getsizeof(r)

		
		#Storing the required data in a variable
			data = 'HTTP/1.0 200 OK'+'\n'+'Content - Length:'+str(sizeoffile)+'\n'+'Content - Type:'+'\n'+ r
		#data1 = r

		#Sending this data to the Client
			connectionSocket.send(data)
		#connectionSocket.sendall(r)
		#connectionSocket.sendall(data1)

			print("File sent")
			connectionSocket.close();

		except Exception as e:
			print("HTTP/1.0 404 File Not Found")
			connectionSocket.sendall("HTTP/1.0 404 File Not Found\r\n\r\n");
			connectionSocket.close();

		# break;


	else:
			#Return an error if the file request format isn't correct
			print("HTTP/1.0 400 Bad Request")
			connectionSocket.sendall("HTTP/1.0 400 Bad Request\r\n\r\n");
			connectionSocket.close();
			# break;


connectionSocket.close();