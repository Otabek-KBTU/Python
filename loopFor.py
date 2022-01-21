h = int(input())
m = int(input())
s = 0
for k in range(h, 24):
    for j in range(m, 60):
        for i in range(0, 60):
            s+=1
            print(s)
        m+=1
        print(m)
        s=0
    h+=1
    m=0
    print(h)
h=0