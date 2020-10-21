def Decoding(n , s):
	C = ''
	if n%2==0:
		for i in range(n-2, -1, -2):
			C +=s[i]
		for j in range(1, n , 2):
			C+=s[j]
	else:
		for i in range(n-2, 0, -2):
			C +=s[i]
		for j in range(0, n , 2):
			C+=s[j]
	return C
n = int(input())
s = str(input())
print(Decoding(n , s))
