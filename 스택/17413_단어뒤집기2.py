S = input()
cnt = S.count("<")
result = ""
print(cnt)

for i in range(cnt):
  start = S.find("<")
  end = S.find(">")

  tag = S[start:end+1]
  S=S.replace(tag, "")
  print(S)
  result+=tag

print(result)

words = S.split()

for word in words:
  result += word[::-1]
  
print(result)