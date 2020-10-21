from itertools import permutations
d= input() ; m= input()
c = d.count('+')-d.count('-')
s = m.count('+')-m.count('-')
j = m.count('?')
pre , k= '' , set()
for i in range(1 , j+1):
	a = i*'+' +(j-i)*'-'
	b = a.count('+') - a.count('-')
	if b== c-s:
		pre = a
		break
	t = i*'-' +(j-i)*'+'
	count = a.count('+') - a.count('-')
	if count == c-s:
		pre = t
		break

for i in permutations(pre):
	k.add(i)
if pre != '':
	print(len(t)/2**j)
else:
	if j ==0 and s == c:
		print(1)
	else:
		print(0)