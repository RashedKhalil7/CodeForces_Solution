n,k = map(int,input().split())
arr = list(map(int,input().split()))
nge = len([i for i in arr if i <0])
for i in range(nge):
	if k==0:
		break
	if arr[i]<0:
		arr[i] *=-1
		k -=1
arr.sort()
if k%2!=0:
	arr[0]*=-1
print(sum(arr))