s = input()
sum1 = 0
sum2 = 0

# 자릿수가 짝수
if len(s) % 2 == 0:
  mid = (0 + (len(s)-1)) // 2
  for i in range(0, mid+1):
    sum1 += int(s[i])
  for j in range(mid+1, len(s)):
    sum2 += int(s[j])

if sum1 == sum2:
  print('LUCKY')
else:
  print('READY')