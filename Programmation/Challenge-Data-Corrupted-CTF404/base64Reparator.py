import socket
import base64
datafinale = ""
test = []
HOST = 'challenge.404ctf.fr'
PORT = 30117
valid = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/']

invalid = "'?!-$(),;.^_ &éè[]<>%*µ£€§~#`{}@à|\\:"+'"'
#=========================================================
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print ('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')
#=========================================================
donnees = client.recv(1024)
donnees += client.recv(512)
base64data = donnees.decode().split(":")[4][1:-3]
print(donnees.decode())
#print (base64data)

while 1:
	#print (base64data)
	if(len(base64data)%4!=0):
		print("decode = non conform base 64")
	#=========================================================
	for x in range(len(invalid)):
	    base64data = base64data.replace(invalid[x],"")
	if(len(base64data)%4!=0):
		print("1st Correct = non conform base 64")
	else :
		print("1st Correct = Conform base 64")
	#=========================================================
	listdata = list(base64data)
	for i in range(len(base64data)):
		c = ord(base64data[i])
		if((65<=c and 90>=c) 
		or (97<=c and 122>=c)
		or (48<=c and 57>=c)
		or c==61 
		or c==43
		or c==47):
			continue
		else :
			if(c == 1040):
				listdata[i] = "A"
			elif(c == 1093):
				listdata[i] = "x"
			elif(c == 1091):
				listdata[i] = "y"
			elif(c == 1072):
				listdata[i] = "a"
			elif(c == 1089):
				listdata[i] = "c"
			elif(c == 1042):
				listdata[i] = "B"
			elif(c == 1053):
				listdata[i] = "H"
			elif(c == 1086):
				listdata[i] = "o"
			elif(c == 1088):
				listdata[i] = "p"
			elif(c == 1077):
				listdata[i] = "e"
			elif(c == 1050):
				listdata[i] = "K"
			elif(c == 1058):
				listdata[i] = "T"
			elif(c == 10):
				listdata[i] = ""
			else:
				print(c)
				print((base64data[i]))	
	base64data = ''.join(listdata) 
	#print(base64data)			

	if(len(base64data)%4!=0):
		print("2nd Correct = non conform base 64")
	else :
		print("2nd Correct = Conform base 64")
	#=========================================================
	while len(base64data)%4!=0 :
		base64data += "="
	if(len(base64data)%4!=0):
		print("3th Correct = non conform base 64")
	else :
		print("3th Correct = Conform base 64")
	#=========================================================
	decoded = base64.decodebytes(base64data.encode("ascii"))
	binary = "".join(["{:08b}".format(x) for x in decoded])
	test.append(binary)
	#print((binary))
	client.send(str(binary+'\n').encode())	
	datafinale +=binary
	print("\n"+binary)
	#=========================================================
	donnees = client.recv(1024)
	if "Wouaouh, tu as réussi !" in (donnees.decode()):
		print(donnees.decode())
		file = open('output', 'w+')
		out = [(hex(int(datafinale[i:i+8], 2))) for i in range(0, len(datafinale), 8)] 
		#file.write(" ".join(out))
		file.write(datafinale)
		file.close()
		input()
		exit()
	base64data = donnees.decode().split(": ")[1][:-3]
	print("==========================================")
	print("\n"+donnees.decode())
	#print(base64data)
	#donnees = client.recv(1024)
	#print(donnees)

client.close()