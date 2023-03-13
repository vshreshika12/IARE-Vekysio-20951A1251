arr=list(input().split())
l=0
for i in arr:
    if len(i)>l:
        l=len(i)
for i in range(len(arr)):
    if len(arr[i])!=l:
        arr[i]='0'*(l-len(arr[i]))+arr[i]
        
for j in range(1,l+1):
    c=[0]*(10)
    for i in arr:
        c[int(i[-j])]+=1
    for i in range(1,len(c)):
        c[i]=c[i-1]+c[i]
    b=[0]*len(arr)

    for i in range(len(arr)-1,-1,-1):
        q=arr[i]
        c[int(q[-j])]-=1
        b[c[int(q[-j])]]=arr[i]
    arr=b
for i in range(len(b)):
    b[i]=int(b[i])
print(b)
