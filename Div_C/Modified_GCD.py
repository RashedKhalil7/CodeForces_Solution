a , b = map(int , input().split())
n = int(input())
for _ in range(n):
	low , high = map(int , input().split())
	for i in range(high , low-1,-1):
		if a%i ==0 and b%i ==0 :
			print(i)
			break
	else:
		print(-1)