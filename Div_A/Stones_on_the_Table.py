n = int(input())
s = input()
count,t = 0 , s[0]
for i in s[1:]:
	if i==t:
		count+=1
		t = i
	else:
		t = i
print(count)