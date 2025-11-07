N = int(input())
num = N

count = 0

while True:
    N2 = N // 10 
    N1 = N % 10 
    N3 = (N1 + N2) % 10 
    N = N1 * 10 + N3 

    count += 1
    
    if N == num:
        break

print(count)
