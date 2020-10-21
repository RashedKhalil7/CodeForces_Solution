lst=[]
for i in range(5):
    lst.append(int(input()))
q=lst[2]*lst[0]
ans=0
while 1:
    if lst[0]>=lst[1]:
        print(0)
        break  
    x=q/(lst[1]-lst[0])
    q+=x*lst[0]
    if q>=lst[4]:
        print(ans)
        break
    ans+=1
    q+=(x+lst[3])*lst[0]
a,b,c,d,e=[int(input())for _ in range(5)]
f=0
while a<b:
    g=(a*c)/(b-a)
    if g*b>=e:
        break
    c+=2*g+d;f+=1
print(f)
bijous=0
vp=int(input())
vd=int(input())
t=int(input())
f=int(input())
c=int(input())
current=0
if vp<vd:
    current=vd * vp * t / (vd-vp)
    while(current<c):
        current = vd * (current + vp * (f + current / vd)) / (vd-vp)
        bijous+=1
print (bijous)