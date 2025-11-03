n, m = map(int, input().split())
basket = []
for x in range(1, n+1):
    basket.append(x)

for y in range(1, m+1):
    i, j = map(int, input().split())
    i = i - 1
    j = j - 1
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp

for b in basket:
    print(b, end=' ')