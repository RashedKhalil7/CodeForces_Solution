n =int(input())
arr = list(map(int,input().split()))
for i in range(n):
	if i ==0:
		m = arr[1]-arr[0]
		x = arr[-1]-arr[0]
	elif i ==n-1:
		m = arr[-1]-arr[-2]
		x = arr[-1]-arr[0]
	else:
		m = min(arr[i]-arr[i-1] ,arr[i+1]-arr[i])
		x = max(arr[-1]-arr[i],arr[i]-arr[0])
	print(m , x)

