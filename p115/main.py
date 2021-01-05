# 행열 입력
input_data = input()
x = int(input_data[1]) # row
y = ord(input_data[0]) - 96 # ex) a1

two = [-2, 2]
one = [-1, 1]

# 경우의 수
num = 0

# 상하
for t in two:
  dx = x + t
  if (dx < 1 or dx > 8):
    continue
  for o in one:
    dy = y + o
    if (dy < 1 or dy > 8):
      continue
    num += 1

# 좌우
for t in two:
  dy = y + t
  if (dy < 1 or dy > 8):
    continue
  for o in one:
    dx = x + o
    if (dx < 1 or dx > 8):
      continue
    num += 1

print(num)