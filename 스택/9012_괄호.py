T = int(input())

for _ in range(T):
  check = input()
  if check.count('(') == check.count(')') and check[0]!=')' and check[-1]!='()':
    print("YES")
  else: print("NO")

