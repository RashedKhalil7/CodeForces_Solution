g , s = [] , set()
n , m , c = map(str,input().split())
n,m = int(n),int(m)
for _ in range(n):
	L=input()
	g.append(L)
for i in range(n):
	for j in range(m):
		if g[i][j] ==c:
			if i-1 >-1:
				s.add(g[i-1][j])
			if i+1 <n:
				s.add(g[i+1][j])
			if j-1 >-1:
				s.add(g[i][j-1])
			if j+1 <m:
				s.add(g[i][j+1])
s -={'.' , c}
print(len(s))
