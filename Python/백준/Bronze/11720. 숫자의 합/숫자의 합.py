N = int(input())
nums = list(map(int, input()))
total = 0

for i in range(0, N):
    total += nums[i]

print(total)
