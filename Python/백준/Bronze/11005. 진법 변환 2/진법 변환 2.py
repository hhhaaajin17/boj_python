n, b = map(int, input().split())
text = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""

if n == 0:
    result = "0"

while n > 0:
    r = n % b
    result = text[r] + result
    n = n // b

print(result)