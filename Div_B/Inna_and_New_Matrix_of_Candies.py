n , m = map(int,input().split())
record = set()
for i in range(n):
	t = input()
	if t.index('G') > t.index('S'):
		print(-1)
		exit()
	else:
		record.add(t.index('S') - t.index('G'))
if record:
	print(len(record))