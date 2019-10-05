a = 50
b = 20

while b > 0:
  tmp = a
  a = b
  b = tmp % b

print(a)