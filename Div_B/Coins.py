Coins = 'ABC'
n = 0
C = ''
D = {c:0 for c in Coins}
for _ in range(3):
	c = str(input())
	if c[1] == '>':
		D[c[0]]+=1
	else:
		D[c[2]]+=1
for i in D:
	if D[i]==2:
		n+=1
if n ==1:
	D = sorted(D.items() , key=lambda x:x[1])
	for i , v in D:
		C+=i
	print(C)
else:
	print('Impossible')

l = [input() for i in range(3)]
dic = {'A':0, 'B':0, 'C':0}
for i in l:
    if i[1]==">":
        dic[i[0]] += 1
    else:
        dic[i[2]]+=1
print("Impossible" if any(i>2 for i in dic.values()) or all(i==1 for i in dic.values()) else ''.join({k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}))
