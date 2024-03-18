nums_string = input()

plus = nums_string.count("+")
minus = nums_string.count("-")

temp = nums_string.replace('-', '+')
nums = list(map(int, temp.split("+")))
nums.sort()

result = 0
cnt = 0
for i in range(plus+1):
  result += nums[i]
  cnt += 1
for i in range(minus):
  result -= nums[cnt+i]

print(result)
