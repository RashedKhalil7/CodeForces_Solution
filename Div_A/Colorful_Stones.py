def cs(s ,t):
	i , j = 0,0
	while i<len(t):
		if t[i]==s[j]:
			j+=1
		i+=1
	return j+1
s = input();t = input()
print(cs(s , t))