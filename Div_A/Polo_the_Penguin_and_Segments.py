n , k = map(int,input().split())
s = 0
for _ in range(n):
	l , r = map(int,input().split())
	s +=r-l+1
t = s%k
if t==0:
	print(t)
else:
	print(k-t)


