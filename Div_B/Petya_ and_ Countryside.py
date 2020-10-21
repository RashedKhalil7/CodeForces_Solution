n  = int(input())
 
sections = list(map(int, input().split()))
max_irri = []
 
 
 
for i in range(n):
    left  = i-1
    right = i +1
    s = 1
    while (left > -1 and sections[left] <= sections[left + 1]):
        s+=1
        left -=1
    while (right < n and sections[right] <= sections[right -1]):
        s+=1
        right+=1
    max_irri.append(s)
print(max(max_irri))