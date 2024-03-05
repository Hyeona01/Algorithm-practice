table = []
max_num = 0

for _ in range(9) :
  table.append(list(map(int,input().split())))

for col in range(0,9) :
  for row in range(0,9) :
    if table[col][row] >= max_num : # 최대 숫자가 0일 경우 주의
      max_col = col+1
      max_row = row+1
      max_num = table[col][row]

print(max_num)
print(max_col, max_row)