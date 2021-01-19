N = map(int, input())

coin = list(map(int, input().split()))
# 3 2 1 1 9

# 작은 단위 동전부터
coin.sort()

# ex) 1 1 2 3 9
# 1부터 target을 탐색
target= 1
for n in coin:
  # target 보다 동전 단위가 크다면
  if target < n:
    break
  target += n

print(target)