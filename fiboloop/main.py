# 피보나치 상향식 방식, 반복문 사용

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
fibo = [0] * 100

# 첫 번째, 두 번째 피보나치 1
fibo[1] = 1
fibo[2] = 1
n = 99

for i in range(3, n+1):
  fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[30])