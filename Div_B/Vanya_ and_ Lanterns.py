a , l =map(int, input().split())
A =list(map(int , input().split()))

A = sorted(A)
n= min(A)
x = max(A)
m = max(n , l-x)
for i in range(len(A)-1):
	if (A[i+1] - A[i])/2 > m:
		m =(A[i+1] - A[i])/2
answer = m
s= format(m , '6f')
m = str(s)+'0000'
print(m)
