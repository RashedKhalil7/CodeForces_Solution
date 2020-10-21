n = int(input())
a = list(map(int, input().split()))
if a ==sorted(a):
	print('yes')
	print(1 , 1 , sep=' ')
else:
	s ,b , e= [] , 0 , 0 
	for i in range(1,n):
		if a[i-1] > a[i]:
			s.append(a[i-1])
			e = i+1
	s.append(a[e-1])
	b = e-len(s)+1
	s.reverse()
	a = a[:b-1]+s+a[e:]
	if a == sorted(a):
		print('yes')
		print(b ,e , sep=' ')
	else:
		print('no')