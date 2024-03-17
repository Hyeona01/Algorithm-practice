n = int(input())
time_list = list(map(int, input().split()))

time_list.sort()

result = 0
for time in time_list:
  result += result
  result += time

print(result)