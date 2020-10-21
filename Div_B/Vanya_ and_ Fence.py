n , h = map(int , input().split())
A = list(map(int , input().split()))
t = 0
for i in range(n):
	if A[i] > h:
		t +=2
	else:
		t+=1
print(t)