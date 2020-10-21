n = input()
t =0
s = 0
while len(n)>1:
	for i in n:
		s += int(i)
	t+=1
	n = str(s)
	s =0
print(t)

'''s=input()
def conv(s):
    return str(sum([int(x) for x in (s)]))
cnt=0
while(len(s)>1):
    cnt+=1
    s=conv(s)
print(cnt)'''
