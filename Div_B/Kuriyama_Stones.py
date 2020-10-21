n = int(input())
s = list(map(int, input().split()))
q = int(input())
a = sorted(s)
s.insert(0 , 0)
a.insert(0 , 0)
for i in range(1,n):
	s[i] = s[i]+s[i-1]
	a[i] = a[i]+a[i-1]
for i in range(q):
	t , l , r = map(int , input().split())
	if t ==1:
		print(s[r] - s[l-1])
	else:
		print(a[r]- a[l-1])