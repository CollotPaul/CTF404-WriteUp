def tour1(password):
    print(str("".join( "".join(password[::-1])[::-1])[::-1]))
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    print([ord(c) for c in string])
    return [ord(c) for c in string]

def tour1decode(password):
    string = ""
    for i in range(len(password)):
    	string += chr(password[len(password)-i-1])
    return string

def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
    print(new)
    return new

def tour2decode(password):
    new = []
    for i in range(len(password)):
    	if i%2==0:
    		new.append(password[i])
    return new

def tour3(password):
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    print(mdp)
    for i in range(len(password)):
    	print("["+str(i)+","+str(len(password) - i -1)+"]","["+mdp[i]+","+mdp[len(password) - i -1 ]+"]",str(i%4),"["+chr(password[len(password) - i -1 ] + i % 4),chr(password[i] + i % 4)+"]")
    	mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i -1 ] + i % 4),  chr(password[i]+ i % 4)
    print(mdp)
    return "".join(mdp)

def tour3decode(password):
    print("==============================")
    mdp = [char for char in password]
    mdpbase =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j','o', 'r', 'y', 'r', 'u', 'a']
    i = len(mdp) -1
    while i > (len(mdp)-1)/2:
    	print(i)
    	mdp_i_prev = chr(ord(mdp[i]))
    	print(mdp_i_prev)
    	mdp_i_prev = chr(ord(mdp[i]) - i % 4)
    	print(mdp_i_prev)
    	print("["+str(i)+","+str(len(password) - i -1)+"]","["+mdp[i]+","+mdp[len(password) - i -1 ]+"]",str(i%4),"["+chr(ord(password[i]) - i % 4),chr(ord(password[len(password) - i -1 ]) - i % 4)+"]")
    	mdp[i], mdp[len(mdp) - i -1 ] = chr(ord(mdp[i]) - i % 4),  chr(ord(mdp[len(mdp) - i -1 ]) - i % 4)
    	#print(mdp)
    	i-=1
    return list(reversed([ord(c) for c in mdp]))


mdp = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"
#input("Mot de passe : ")
#print(tour1decode(tour1(mdp)))

print(tour1decode(tour2decode(tour3decode(mdp))))