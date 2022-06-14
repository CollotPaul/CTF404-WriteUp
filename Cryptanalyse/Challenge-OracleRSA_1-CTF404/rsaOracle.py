import socket
from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA
from binascii import hexlify,unhexlify

HOST = 'challenge.404ctf.fr'
PORT = 32128

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
donnees = client.recv(1024)
while ">" not in donnees.decode():
	donnees += client.recv(1024)
	
print(donnees.decode())
flag = int(donnees.decode().split("!")[1][1:].split('\n')[0])
N = int(donnees.decode().split("=")[1][1:-2].split('\n')[0])
e = int(donnees.decode().split("=")[2][1:].split('\n')[0])
print("flag :",str(flag)+"\n")
print("N :",N)
print("e :",e)

message=b'test'
print(hexlify(message))
mes=int(hexlify(message),16)
s=14  #I can chose a random number
t=pow(s,e)
c1=(t*flag)%N
client.send((str(c1)+"\n").encode())
donnees = client.recv(1024)
response = donnees.decode().split(":")[1].split("\n")[1]
print(response)
m1 = int(response)
#m1=10208904974004529353197158859950332747467331900144632208359634050163402208513308498268725060661210
r=inverse(m1,N)
plain_text=inverse(r*s,N)
g=hex(plain_text)[2:].strip('L')

print(unhexlify(g))
client.close()