n  ,k = map(int , input().split())
arr = list(map(str,input().split()))
s = 0
for i in arr:
	a = i.count('4')
	b = i.count('7')
	if a+b <=k:
		s +=1
print(s)
