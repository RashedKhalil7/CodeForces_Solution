n = int(input()); arr = sorted(list(map(int,input().split())))
m,t , s = max(arr) ,0 , 0
for i in range(1,n-1):
	if arr[i-1]+arr[i] > arr[i+1]:
		print('YES')
		break
else:
	print('NO')