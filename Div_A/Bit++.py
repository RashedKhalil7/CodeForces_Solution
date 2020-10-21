t = 0
for _ in range(int(input())):
	op = input()
	if '++'in op:t+=1
	else:t-=1
print(t)