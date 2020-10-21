n , k = map(int , input().split())
d = [0]*n
for _ in range(k):
	a , b ,c = map(int,input().split())
	d[a-1]+=c
	d[b-1]-=c
print(sum(x for x in d if x>0))