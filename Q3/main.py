# 문자열을 숫자 리스트로 변환
s = list(map(int, input()))

num0 = 0
num1 = 0

for i in range(len(s)):
  # 0의 부분 갯수
  if s[i] == 0:
    continue
  if s[i-1] == 0:
    num0 += 1

for i in range(len(s)):
  # 1의 부분 갯수
  if s[i] == 1:
    continue
  if s[i-1] == 1:
    num1 += 1

print(min(num0, num1))
