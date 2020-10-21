n = int(input())
v = ['R', 'O', 'Y', 'G', 'B', 'I', 'V']
E = [0]*n
E[:7] = "".join(v)
for i in range(7,n):
	E[i]=E[i-4]
print("".join(E))