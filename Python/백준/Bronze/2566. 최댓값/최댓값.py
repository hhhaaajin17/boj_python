num = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
row, col = 0, 0

for i in range(9):
    for j in range(9):
        if num[i][j] >= max_num:
            max_num = num[i][j]
            row = i
            col = j

print(max_num)
print(row+1, col+1)
