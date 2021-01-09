# 피보나치 재귀함수 방식 + 메모이제이션
# 메모이제이션 : 한 번 해결한 문제를 저장해두었다 다시 호출하여 사용

# 메모제이션 저장소
memo = [0] * 100

def fibo(x):
  if x==1 or x==2:
    return 1
  if memo[x] != 0:
    return memo[x]

  memo[x] = fibo(x-1) + fibo(x-2)
  return memo[x]

print(fibo(6))