a = int(input())
b = int(input())
c = int(input())
if (a % 2 == 0 or b % 2 == 0 or c % 2 == 0) or (a != b and b != b and a != c):
    print("YES")
else:
    print("NO")
