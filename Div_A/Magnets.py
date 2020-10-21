n = int(input());c , s = 0 ,1
for i in range(n):
	m = input()
	if i <1:
		c = m
	else:
		if c !=m:
			s +=1;c = m
print(s)