a =list(map(int, input().split()))
n = list(map(int , input()))
count =0 
for i in range(4):
	count +=n.count(i+1)*a[i]
print(count)