n = int(input())
arr = set(map(int , input().split()))
if len(arr)<3:
	print('YES')
if len(arr) >3:
	print('NO')
else:
	arr = sorted(list(arr))
	if 2*arr[1]== arr[0]+arr[2]:
		print('YES')
	else:
		print('NO')