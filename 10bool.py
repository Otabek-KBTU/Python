h=int(input())
min = int(input())
sec=0
while h!=24:
    while min!=60:
        while sec !=60:
            sec += 1
            print(sec)
        min += 1
        print(min)
        sec = 0
    h+=1
    min = 0
    print(h)
h=0