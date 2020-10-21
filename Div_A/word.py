s = input()
l , u = 0 ,0
for i in s:
	if ord(i) > 91:
		l +=1
	if ord(i) < 91:
		u +=1
if l>=u:
	print(s.lower())
if l <u:
	print(s.upper())