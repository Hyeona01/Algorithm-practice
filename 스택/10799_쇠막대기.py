S = input()

# 레이저가 있는 시점에 쇠막대기가 몇개인지 -> pipe
# 여는 괄호 이후에 레이저를 만나면 +pipe, 닫힌 괄호에서 +1
pipe = 0
total_pipe = 0

for i in range(0,len(S)-1):
  if S[i] == '(':
    if S[i+1] == ')':
      total_pipe += pipe
    else: pipe += 1
  elif S[i] == ')':
    if S[i-1] == '(':
      continue
    else:
      pipe -= 1
      total_pipe += 1
total_pipe += 1

print(total_pipe)