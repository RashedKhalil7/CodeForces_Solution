def solve(d):
	l ,n= len(d) , int(d[0])
	return 10*(n-1)+(l*(l+1))//2
for _ in range(int(input())):
	p = input()
	print(solve(p))
