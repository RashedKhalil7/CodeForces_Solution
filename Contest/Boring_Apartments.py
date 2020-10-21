def solve(p):
	d = 
	d,l,p = {1:1,2:3,3:6,4:10},len(p) , int(p[:1])
	if l==1==p:print(1)
	elif l==4:print(p*d[l])
	else:
		n = str(p-1)+str(d[l])
		print(int(n))
for _ in range(int(input())):
	p = input()
	solve(p)		
