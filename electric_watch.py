num = int(input())
a = ((num % 1440) // 60) % 24
b = num % 60
print(a, b)
