import socket
import time
import os
import sys

#get the start arguments in console so we read the arguments
#in the start from the python program

helpfile = """

EvilEx - helpfile with examples and arguments

--target <Target> | Selecting/change the target to that was selecting
 -t      <Target> | Selecting/change the target to that was selecting
--port   <Port>   | Selecting/change the port to that then sending payload
 -p      <Port>   | Selecting/change the port to that then sending payload
--file   <file>   | Selecting/change the file that was then sending to the target port
 -f      <file>   | Selecting/change the file that was then sending to the target port

example:  python3 EvilEx.py --target <Target> --port <Port> --file <Payload>
example:  python3 EvilEx.py -t <Target> -p <Port> -f <Payload>
example:  python3 EvilEx.py --target <Target> -p <Port> -f <Payload>
example:  python3 EvilEx.py -t --port <Port> --file <Payload>
example:  python3 EvilEx.py --target <Target> -p <Port> --file <Payload>

info: It have other examples but i cant write it all in the helpfile
      did you know me?

"""

try:
	if sys.argv[1] == '--target':
		host = str(sys.argv[2])
		host = socket.gethostbyname(host)
		if sys.argv[3] == '--port':
			port = int(sys.argv[4])
			if sys.argv[5] == '--file':
				file = str(sys.argv[6])
			elif sys.argv[7] == '-f':
				file = str(sys.argv[8])
			else:
				print(helpfile)
				sys.exit()
		elif sys.argv[3] == '-p':
			port = int(sys.argv[4])
			if sys.argv[5] == '--file':
				file = str(sys.argv[6])
			elif sys.argv[7] == '-f':
				file = str(sys.argv[8])
			else:
				print(helpfile)
				sys.exit()
		else:
			print(helpfile)
			sys.exit()
	elif sys.argv[1] == '-t':
		host = str(sys.argv[2])
		host = socket.gethostbyname(host)
		if sys.argv[3] == '--port':
			port = int(sys.argv[4])
			if sys.argv[5] == '--file':
				file = str(sys.argv[6])
			elif sys.argv[7] == '-f':
				file = str(sys.argv[8])
			else:
				print(helpfile)
				sys.exit()
		elif sys.argv[3] == '-p':
			port = int(sys.argv[4])
			if sys.argv[5] == '--file':
				file = str(sys.argv[6])
			elif sys.argv[5] == '-f':
				file = str(sys.argv[6])
			else:
				print(helpfile)
				sys.exit()
		else:
			print(helpfile)
			sys.exit()
	else:
		print(helpfile)
		sys.exit()
except Exception as argumentError:
	print(helpfile)
	sys.exit()

#at here begin the mainscript

sep = "#SEP#"
if sep in file:
	print("[+] [warning] WARNING INVALID FILE NAME!")
	sys.exit()
file_size = os.path.getsize(file)
stream = socket.socket()
print("[+] [EVILEX] Testing Connection to target url/address")
time.sleep(4)
try:
	stream.connect((host, port))
	print("[+] [EVILEX] Connection to target url/address succes!")
	print(f"[+] [EVILEX] Connection to: Target: {host} Port: {Port}")
	stream.send(f"{file}{file_size}".encode())
	buffer = int(input("[+] [BUFFER] Set the sending buffer [Default: 1024]: "))
	print("[+] [EXPLOITATION] Sending evil Payload to target url/address server")
	with open(file, "rb") as f:
		while True:
			file_bytes = f.read(buffer)
			if not file_bytes:
				print("[+] [EVILEX] Sending evil Payload to target url/address server succes!")
				sys.exit()
			stream.sendall(file_bytes)
except:
	print("[+] [EVILEX] There was an error! Sending or Connection failed!")
	sys.exit()