# 맵 생성
N, M = map(int, input().split())

# 좌표, 방향 입력
x, y, direction = map(int, input().split())

# 동서남북 좌표
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

num = 0

# 맵 생성1
m = []
for i in range(N):
  m.append(list(map(int, input().split())))
# 시작지점
m[x][y] = 'x' # 밟은 땅으로 표시

# 왼쪽 확인
count = 0

while True:
  while(count<4):
    left = direction-1
    if(direction == 0):
      left=3
    if (m[x + dx[left]][y + dy[left]] == 0):
      # 방향 바꾸기
      if(direction==0):
        direction = 3
      else:
        direction -= 1
      # 좌표 바꾸기
      m[x][y] = 'x' # 밟은 땅을 x로 표시
      x = x + dx[left]
      y = y + dy[left]

      count = 0
    else: # 이미 밟거나 바다인 경우 방향만 전환
      # 방향 바꾸기
      if(direction==0):
        direction = 3
        count += 1
      else:
        direction -= 1
        count += 1

  # 방향 유지, 뒤로 한칸
  left = direction-1
  if(direction == 0):
    left=3
  back = left - 1
  if(left == 0):
    back = 3

  if(m[x + dx[back]][y + dy[back]]==1): # 뒤가 바다면
    for row in m:
      num += row.count('x')
    print(num)
    exit(0)
  else:
    m[x][y] = 'x' # 밟은 땅을 x로 표시
    x = x + dx[back]
    y = y + dy[back]
    

