w = []
col = ['Carrots', 'Kiwis', 'Grapes']
n , m , k , t = map(int,input().split())
for _ in range(k):
	w.append(list(map(int, input().split())))
for _ in range(t):
	c = list(map(int,input().split()))
	if c in w:
		print('Waste')
	else:
		s=0
		for i in w:
			if i < c:
				s +=1
		val = (c[0]-1)*m + c[1]-1 -s
		print(col[val%3])