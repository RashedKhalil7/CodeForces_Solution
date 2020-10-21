n , t1 , t2 , k = map(int,input().split()) ; result, res = {} , {}
a = {i:list(map(int,input().split()))for i in range(1,n+1)}
for i in range(1 , n+1):
	s =(a[i][0]*t1)- (a[i][0]*t1*(k/100)) +(a[i][1]*t2)
	t = (a[i][1]*t1)- (a[i][1]*t1*(k/100)) +(a[i][0]*t2)
	s = format(max(s , t) , '.2f')
	res[i] = s
	result[i]=float(s)
result = sorted(result.items() , key = lambda x:x[1], reverse=True)
for i,j in result:
	print(i , res[i])