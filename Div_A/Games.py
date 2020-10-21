a , b = [] , []
n = int(input())
for i in range(n):
	h , g = map(int,input().split())
	a.append(h) ; b.append(g)
t = 0
for i in range(n):
	t += b.count(a[i])
print(t)
