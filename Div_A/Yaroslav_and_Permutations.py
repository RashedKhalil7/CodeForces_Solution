n = int(input())
arr = list(map(int,input().split()))
arri = sorted([arr.count(i) for i in set(arr)])
a = arri[-1]
print('YES' if a*2-1<=n else 'NO')
