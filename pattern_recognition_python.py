def find_patern(a):
	i=1
	while i<len(a)//2:
		lena = len(a)-len(a)%i
		if a[:lena]==a[:i]*int(lena/i):
			print(a[:i]+ ' is a patern of '+a)
			print ("there is garbage in your sequence :"+a[lena+1:])
			return
		i+=1
	print ('No patern')

for key in l_keys:
	A[key[0]][key[1]]=scor_count[key]