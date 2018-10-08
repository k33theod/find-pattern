def find_patern(a):
	i=1
	while i<len(a)//2:
		lena = len(a)-len(a)%i
		if a[:lena]==a[:i]*int(lena/i):
			print(a[:i]+ ' is a patern of '+a)
			print ("there is garbage in your sequence :"+a[lena+1:])
			return a[:i]
		i+=1
	print ('No patern')

