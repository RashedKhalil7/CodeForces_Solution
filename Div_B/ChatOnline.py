x ,z, t= set() , set() , 0
p , q , l ,r = map(int , input().split())
for i in range(p):
	a , b = map(int,input().split())
	for i in range(a , b+1):
		z.add(i)
for j in range(q):
	c ,d = map(int,input().split())
	for i in range(c , d+1):
		x.add(i)
for i in range(l , r+1):
	for j in x:
		if j+i in z:
			t +=1
			break
print(t)
