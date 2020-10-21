n = int(input())
a =list(map(int,input().split()))
a1 , a2 , a3 = [],[],[]
m= min(a.count(1) , a.count(2) , a.count(3))
print(m)
for i in range(n):
	if a[i]==1:
		a1.append(i)
	if a[i]==2:
		a2.append(i)
	if a[i] == 3:
		a3.append(i)
for i , j , k in zip(a1[:m],a2[:m],a3[:m]):
	print(i+1 ,j+1 ,k+1)