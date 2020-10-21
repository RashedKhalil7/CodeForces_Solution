n, d = map(int, input().split())
p=list(map(int, input().split()))
for j in range(n):
	if j ==0:
		p[j] = p[j]
	else:
		p[j] = p[j]+p[j-1]
d -=1
s =p[d]
mi = 0
for i in range(1 , n-d):
	t = p[d+i]-p[i-1]
	if s > t:
		s = t
		mi = i
print(mi+1)