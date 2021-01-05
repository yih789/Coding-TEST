# N, M, K 입력
N, M, K = map(int, input().split())
# N개의 데이터 입력
data = list(map(int, input().split()))

# 내림차순 정렬
data.sort(reverse=True)

# 합계 초기화
sum = 0

while(True):
  for i in range(K):
    if( M == 0 ): break
    sum += data[0]
    M -= 1
  if( M == 0): break
  sum += data[1]
  M -= 1

print(sum)