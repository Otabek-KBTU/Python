t = int(input())
h = t // 3600 % 24
m = t // 60 % 60
s = t % 60
print(h, ":", m//10, m % 10, ":", s//10, s % 10, sep="")
