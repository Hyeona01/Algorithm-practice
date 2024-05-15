T = int(input())
lst = []
lst_reverse = [T]

for i in range(T):
  temp = ""
  lst = list(map(str,input().split()))
  
  for j in range(len(lst)):
    temp += lst[j][::-1] + " "
  print(temp)