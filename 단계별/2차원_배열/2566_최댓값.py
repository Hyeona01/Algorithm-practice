max_num, row, col = 0, 0, 0
row = []

for i in range(1, 10):
  row = list(map(int,input().split()))
  if max(row) > max_num :
    max_num = max(row)
    row = i
    col = row.index(str(max_num))

print(max_num, row, col)