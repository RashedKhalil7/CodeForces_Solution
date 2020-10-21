s1 =sorted(list(map(int,input().split('+'))));s=''
s +=str(s1[0]);s2 =''.join(['+'+str(i)for i in s1[1:]])
print(s+s2)