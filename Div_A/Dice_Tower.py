n = int(input()) ;t = int(input())
for _ in range(n):
	a , b = map(int,input().split())
	if 7-t in (a,b)or t in (a,b):
		print('NO')
		exit()
print('YES')

