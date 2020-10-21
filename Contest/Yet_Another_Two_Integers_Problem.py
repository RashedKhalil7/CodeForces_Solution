t = int(input())
for _ in range(t):
	a , b = map(int,input().split())
	if abs(int(a-b))%10 == 0:
		print(abs(int((b-a)/10)))
	else:
		print(abs(int((b-a)/10))+1)


