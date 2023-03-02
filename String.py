#Recursion
def rev(l,a):
    if(a==len(l)):
        return ""
    else:
        def rere(s,j):
            if(j<0):
                return " "
            else:
                return s[j]+rere(s,j-1)

        s1=(rere(l[a],len(l[a])-1))
        return s1+rev(l,a+1)       
s=input()
l=list(s.split())
a=0
print(rev(l,a))


#Multi Threading
import threading

def print_revstr(q):
    print(q[::-1],end='')
    
def Space():
    print(end=' ')

s=input()
s=list(s.split())
for i in range(0,len(s),2):
    t1 = threading.Thread(target=print_revstr, args=(s[i],))
    t2=threading.Thread(target=Space)
    if(i+1<len(s)):
        t3 = threading.Thread(target=print_revstr, args=(s[i+1],))
    t4=threading.Thread(target=Space)
    t1.start()
    t2.start()
    if(i+1<len(s)):
        t3.start()
    t4.start()
    t1.join()
    t2.join()
    if(i+1<len(s)):
        t3.join()
    t4.join()


