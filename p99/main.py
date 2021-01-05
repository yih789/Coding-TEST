# N, K를 입력
N, K = map(int, input().split())

# 최소 연산횟수
count = 0

# N을 K의 배수로 만든다.
while( N!=1 ):
  if(N%K==0):
    N /= K
    count += 1
  else:
    while(N%K!=0):
      N -= 1
      count += 1

print(count)

