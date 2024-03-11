n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
result = 0

nums.sort()

while m > 0 :
  for _ in range(k):
    if m > 0 :
      result += nums[-1]
      m -= 1
    else :
      break

  if m > 0 :
    result += nums[-2]
    m -= 1
  else :
    break

print(result)