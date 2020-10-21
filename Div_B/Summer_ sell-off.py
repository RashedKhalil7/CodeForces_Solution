d ,t = [] , 0
n , f = map(int,input().split())
for _ in range(n):
	k , l = map(int,input().split())
	#k represent product in that day to sell , l represent client in that day
	t +=min(k ,l)
	d.append(min(k*2 , l) - min(k ,l))
d.sort()
t+= sum(d[n-f:])
print(t)
