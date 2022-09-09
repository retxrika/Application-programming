a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print((a + b) / 2)

if a < 0:
    a = -a
if b < 0:
    b = -b

if a > b:
    print(a - b)
else:
    print(b - a)