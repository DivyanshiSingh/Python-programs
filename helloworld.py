import random
alphabets="qwertyuiopasdfghjklzxcvbnm"
alphabets=list(alphabets)
# while("".join(alphabets[0:11])!="helloworld"):
j=1
while(1):
	l=[]
	for i in range(5):
		temp=random.choice(alphabets)
		l.append(temp)
	print(j,"".join(l))
	j+=1
	if("".join(l)=="python"):
		break