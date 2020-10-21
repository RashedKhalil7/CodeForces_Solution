n = int(input())
arr = list(map(int,input().split()))
for i in range(1,n):
	if i==0:
		arr[i] = arr[i]
	else:
		arr[i] = arr[i]+arr[i-1]
lis = []
for i in range(1,4):
	lis.append(arr.count(arr[-1]//3*i))
print(lis)