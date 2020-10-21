n , m = map(int , input().split())
p = list(map(int , input().split()))
best = 1000000
p.sort()
for i in range(m-n+1):
	best = min(p[n+i-1] -p[i],best)
print(best)