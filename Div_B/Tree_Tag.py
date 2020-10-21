from collections import defaultdict
g = defauldict(list)


t = int(input())
for i in range(t):
	n , a , b , da , db= map(int,input().split())
	for i in range(n-1):
		u , v = map(int,input().split())
		g[u].append(v)
		g[v].append(u)