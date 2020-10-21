n, a = map(int, input().split())
ar = list(map(int, input().split()))
a = a-1
b = min(a+1 , n-a)
count =0
count +=ar[a]
for i in range(1,b):
	l = a-i
	r = a+i
	if ar[l] + ar[r]==2:
		count+=2
if a < n-a:
	for i in range(a+1,n-a):
		count +=ar[a+i]
if a > n-a:
	b = n-a-1
	count +=sum(ar[0:a-b])
print(count)



s = []
l = 0
a=a+1
for i in range(n):
    if ar[i] == 1:
        s.append(i+1)
for i in range(1, n):
    if a-i in s and a+i in s:
        l+=2
    if a+i in s and a-i<=0:
        l+=1
    if a-i in s and a+i>=n+1:
        l+=1
print(l+int(ar[a-1]==1))