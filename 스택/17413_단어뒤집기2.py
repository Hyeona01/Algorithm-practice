S = input()

# S 한 글자씩 체크, < 가 나오면 >가 나올 때까지 그대로 push
# < 가 나오지 않으면 띄어쓰기가 나올 때까지 별도 리스트에 Push, 띄어쓰기 만나면 역순 출력

temp = ""
result = ""
is_tag = False

for i in S:
  if i == "<":
    is_tag = True
    result += temp[::-1]
    temp = ""
  elif i == ">": 
    is_tag = False
    result += i
    continue

  if is_tag:
    result += i
  else:
    if i != " ": temp += i
    else: 
      result += temp[::-1] + " "
      temp = ""
  # print("temp: ", temp, "result:", result)

result += temp[::-1]
print(result)