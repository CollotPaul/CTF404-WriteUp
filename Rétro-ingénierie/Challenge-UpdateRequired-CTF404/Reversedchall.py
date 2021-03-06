#!/usr/bin/python3.10
import random as rd

s = [16, 3, 12, 9, 1, 60, 1, 3, 14, 39, 13, 16, 16, 1, 9, 13, 3, 39, 60,
    16, 16, 1, 60, 7, 39, 13, 3, 13, 18, 3, 13, 25, 14, 3, 1, 14, 60,
    13, 32, 13, 3, 39, 16, 18, 18, 3, 43, 16, 18, 3, 1, 43, 18, 16,
    13, 16, 1, 3, 1, 16, 13, 18, 60, 16, 3, 3, 14, 18, 13, 14, 16, 18,
    7, 3, 7, 25, 7, 7, 13, 13, 13, 3, 60, 1, 3, 13, 1, 25, 18, 16, 32,
    16, 60, 1, 7, 44, 18, 39, 39, 39, 60, 3, 1, 60, 3, 16, 13, 13, 14,
    1, 3, 39, 39, 31, 32, 39, 32, 18, 39, 3, 13, 32, 60, 7, 7, 39, 14,
    3, 18, 14, 60, 39, 18, 7, 1, 32, 13, 3, 14, 39, 39, 7, 1, 1, 13,
    29, 60, 13, 39, 14, 14, 16, 60, 1, 3, 44, 14, 3, 1, 1, 1, 39, 13,
    14, 39, 18, 3, 7, 13, 39, 32, 1, 43, 1, 16, 1, 3, 18, 14, 25, 32,
    7, 13, 39, 7, 1, 3, 60, 13, 13, 7, 18, 1, 3, 18, 1, 60, 7, 1, 39,
    14, 3, 39, 7, 31, 1, 7, 18, 7, 32, 3, 3, 14, 32, 14, 1, 32, 12,
    18, 31, 39, 1, 13, 13, 43, 44, 32, 3, 32, 60, 14, 60, 60, 7, 3, 1,
    3, 3, 14, 1, 60, 16, 44, 3, 1, 32, 13, 5, 16, 39, 3, 60, 7, 14, 3,
    13, 7, 31, 13, 39, 9, 3, 44, 13, 16, 14, 18, 18, 3, 7, 3, 3, 3, 7,
    3, 3, 16, 39, 3, 3, 13, 32, 13, 3, 18, 7, 10, 3, 18, 1, 7, 7, 18,
    13, 43, 18, 3, 32, 39, 32, 13, 1, 18, 10, 1, 32, 1, 16, 32, 3, 44,
    3, 18, 1, 1, 1, 16, 18, 25, 60, 1, 39, 1, 18, 60, 16, 1, 7, 3, 13,
    16, 18, 39, 14, 7, 14, 3, 14, 13, 7, 16, 10, 18, 13, 3, 16, 13, 3,
    32, 43, 13, 14, 1, 13, 1, 14, 18, 60, 7, 3, 7, 31, 1, 18, 26, 7,
    3, 3, 32, 1, 7, 18, 7, 1, 16, 18, 39, 14, 7, 3
]

truelist = [11, 7, 15, 14, 4, 9, 4, 7, 3, 6, 8, 11, 11, 4, 14, 8, 7, 6, 9, 11, 11, 4, 9, 10, 6, 8, 7, 8, 5, 7, 8, 12, 3, 7, 4, 3, 9, 8, 2, 8, 7, 6, 11, 5, 5, 7, 1, 11, 5, 7, 4, 1, 5, 11, 8, 11, 4, 7, 4, 11, 8, 5, 9, 11, 7, 7, 3, 5, 8, 3, 11, 5, 10, 7, 10, 12, 10, 10, 8, 8, 8, 7, 9, 4, 7, 8, 4, 12, 5, 11, 2, 11, 9, 4, 10, 13, 5, 6, 6, 6, 9, 7, 4, 9, 7, 11, 8, 8, 3, 4, 7, 6, 6, 0, 2, 6, 2, 5, 6, 7, 8, 2, 9, 10, 10, 6, 3, 7, 5, 3, 9, 6, 5, 10, 4, 2, 8, 7, 3, 6, 6, 10, 4, 4, 8, 17, 9, 8, 6, 3, 3, 11, 9, 4, 7, 13, 3, 7, 4, 4, 4, 6, 8, 3, 6, 5, 7, 10, 8, 6, 2, 4, 1, 4, 11, 4, 7, 5, 3, 12, 2, 10, 8, 6, 10, 4, 7, 9, 8, 8, 10, 5, 4, 7, 5, 4, 9, 10, 4, 6, 3, 7, 6, 10, 0, 4, 10, 5, 10, 2, 7, 7, 3, 2, 3, 4, 2, 15, 5, 0, 6, 4, 8, 8, 1, 13, 2, 7, 2, 9, 3, 9, 9, 10, 7, 4, 7, 7, 3, 4, 9, 11, 13, 7, 4, 2, 8, 19, 11, 6, 7, 9, 10, 3, 7, 8, 10, 0, 8, 6, 14, 7, 13, 8, 11, 3, 5, 5, 7, 10, 7, 7, 7, 10, 7, 7, 11, 6, 7, 7, 8, 2, 8, 7, 5, 10, 18, 7, 5, 4, 10, 10, 5, 8, 1, 5, 7, 2, 6, 2, 8, 4, 5, 18, 4, 2, 4, 11, 2, 7, 13, 7, 5, 4, 4, 4, 11, 5, 12, 9, 4, 6, 4, 5, 9, 11, 4, 10, 7, 8, 11, 5, 6, 3, 10, 3, 7, 3, 8, 10, 11, 18, 5, 8, 7, 11, 8, 7, 2, 1, 8, 3, 4, 8, 4, 3, 5, 9, 10, 7, 10, 0, 4, 5, 23, 10, 7, 7, 2, 4, 10, 5, 10, 4, 11, 5, 6, 3, 10, 7]
##
def a(c, r=True):
    #print("==A==")
    # Converti le caract??re en unicode
    n = ord(c)
    #print(n," : ", c)
    #Si r est ?? True g??n??re la seed n pour l'al??atoire
    if r: rd.seed(n)
    #print(r,n)
    match n:
        case 0:
            return dict.fromkeys(range(10), 0)
        case _:
            return (d:=a(chr(n - 1), False)) | {(m:=rd.randint(0, 9)): d[m] + rd.randint(0,2)}

##

def b(p, n):
    #print("===B===")
    match list(p):
        case []:
            return []
        case [f, *rest]:
            #print(f, rest)
            (reada:=a(f).values())
      
            l = list(reada) + b(''.join(rest), n*2)
            #print(l)
            return l
            rd.seed(n)
            rd.shuffle(l)
            #print(l)
            return l

##
#truelist = [0]*len(s)
def c(p, n=0,j=0):
    print("====C====")
    #print(p)
    match p:
        case []:
            return n!=0
        case [f, *rest]:
            rd.seed(s[n])
            print(a:=rd.randint(0,30),a==f,j)
            if(a!=f):
            	truelist[j]=a
            	#print(truelist)
            else:
            	j+=1
            return a == f and c(rest, n + 1,j)
##
valid = ['=','<','>','&','_','!','?','#','-','"',"'",'.',':','@','{','}','(',')','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','+','/','_','*']

#print(c(truelist,0))

#for i in range(len(valid)):
#	#print(valid[i])
#	l=b(valid[i], 1)
#	nb = 0
#	for j in l:
#		if j in truelist:
#			nb +=1
#	if nb == len(l):
#		print(valid[i])
#if c(b(input("password:"), 1)):
#    print("Utilise ce mot de passe pour valider le challenge!")
#else:
#    print("Essaye Encore!")
import random 

def shuffle_under_seed(ls, seed):
  # Shuffle the list ls using the seed `seed`
  random.seed(seed)
  random.shuffle(ls)
  return ls
  
def unshuffle_list(shuffled_ls, seed):
  n = len(shuffled_ls)
  # Perm is [1, 2, ..., n]
  perm = [i for i in range(1, n + 1)]
  # Apply sigma to perm
  shuffled_perm = shuffle_under_seed(perm, seed)
  # Zip and unshuffle
  ls = list(zip(shuffled_ls, shuffled_perm))
  ls.sort(key=lambda x: x[1])
  return [a for (a, b) in ls]
  
#print(truelist)
#truelist = unshuffle_list(truelist,1)
#print(truelist)
#for i in range(len(valid)):
#	print(b(valid[i],1))
l=b('4', 1)
#nb = 0
print(l)
#for j in range(len(l)):
#	if l[j]==truelist[j]:
#		nb +=1
#if nb == len(l):
#	print(valid[i])

n = 1
flag = ""
for i in range(38):
	truelist = unshuffle_list(truelist,n)

	caracterelist = truelist[:10]
	#print(caracterelist)
	truelist = truelist[10:]
	for j in range(len(valid)):
		l = b(valid[j],1)
		#print(l,caracterelist)
		nb = 0
		for h in range(len(l)):
			if l[h]==caracterelist[h]:
				nb+=1
		if(nb == 10):
			flag += (valid[j])
	n=n*2
print(flag)
				
	