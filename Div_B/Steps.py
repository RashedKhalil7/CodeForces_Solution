import math
def step(f , r , k):
	if k==0:
		return math.inf
	if k < 0:
		return -int((r-1)/k) 
	return int((f-r)/k)
n , m = map(int,input().split())
x , y = map(int,input().split())
d = int(input())
ans = 0
for i in range(d):
	i , j = map(int,input().split())
	steps = min(step(n , x , i ) ,step(m , y , j))
	x +=steps*i ; y +=steps*j
	ans +=steps
print(ans)