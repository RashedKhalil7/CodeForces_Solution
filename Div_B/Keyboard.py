key , shift = [] , []
n , m , x = map(int,input().split())
for i in range(n):
	key.append(input())
q = int(input())
t = input()

for i in range(n):
	for j in range(m):
		if key[i][j] == 'S':
			shift.append((i,j))
		else: