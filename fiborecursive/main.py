# 피보나치 수열을 재귀함수로 나타내기
# 탑다운 방식
def fibo(x):
  if x==1 or x==2:
    return 1
  return fibo(x-1) + fibo(x-2)

print(fibo(5))