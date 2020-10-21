'''s=input();a="qwertyuiopasdfghjkl;zxcvbnm,./"
for l in input():print(a[a.index(l)+[1,-1][s=='R']],end='')'''
arr = 'qwertyuiopasdfghjkl;zxcvbnm,./'
def pos(t , arr, n):
	r = ''
	for i in t:
		ind = arr.index(i)
		ind = ind+n
		r +=arr[ind]
	return r
k = input()
t = input()
if k =='R':
	print(pos(t , arr , -1))
if k == 'L':
	print(pos(t , arr , 1))