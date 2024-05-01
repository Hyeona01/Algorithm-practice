T = int(input())
lst = []

for i in range(T):
  lst = list(map(str,input().split()))
  
  for j in range(len(lst)):
    print(lst[i][-1])

# print(lst)