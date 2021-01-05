# 행열 받기
N, M = map(int, input().split())

# 첫 번째 행
data = list(map(int, input().split()))
max = min(data)

for _ in range(N-1):
  # 나머지 행
  data = list(map(int, input().split()))
  if(max < min(data)):
    max = min(data)

print(max)