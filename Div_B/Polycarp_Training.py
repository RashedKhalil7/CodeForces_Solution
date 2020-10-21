x = int(input())
arr = sorted(list(map(int ,input().split())))
pos = 1
for i in range(x):
	if pos <=arr[i]:
		pos+=1
print(pos-1)