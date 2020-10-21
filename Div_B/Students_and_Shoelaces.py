n , m = map(int,input().split())
G = {i:set() for i in range(n+1)}
for i in range(m):
	u , v = map(int,input().split())
	G[u].add(v)
	G[v].add(u)
def counting(G):
	g =0
	while True:
		ans = []
		c = 0
		for i in G:
			if len(G[i])==1:
				G[i] = set()
				c = 1
				ans.append(i)
		if c:
			for i in ans:
				for j in G:
					if m in G[j]:
						G[j].discard(m)
		else:
			break
		g +=1
	print(g)

counting(G)

