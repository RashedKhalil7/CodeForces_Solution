def linear_search(arr):
	d=dict()
	for j in range(len(arr)):
		d[arr[j]] =j
		# we use dict here to use array element as a key and its index as a value
		#d = {1 : 0 , 3: 1 , 2:2} to less time consumes it does loop one time instead doing it more than 1
	return d 

p , s = 0 ,0
t = int(input())
arr = list(map(int , input().split()))
q = int(input())
qn= list(map(int , input().split()))
d = linear_search(arr)
for j in range(q):
	s += d[qn[j]]+1
	p += t- d[qn[j]]
print(s , p)
'''
n = int(input())
a = {a:i for i, a in enumerate(map(int, input().split()))}
m = int(input())
b = sum(a[i] for i in map(int, input().split()))
print(b+m, n*m-b)'''