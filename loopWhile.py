h=int(input())
m=int(input())
s=0
while h!=24:
    while m!=60:
        while s!=60:
            s+=1
            print(s)
        m+=1
        print(m)
        s=0
    h+=1
    m=0
    print(h)
h=0
