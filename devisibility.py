a = int(input())
b = int(input())
print('YES'*(((a//b)-(a % b))//(a//b))+'NO'*((((a % b)+2)//((a % b)+1)) % 2))
