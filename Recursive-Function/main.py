# 자기 자신을 호출하는 함수
# if문으로 종료조건을 명시해야 무한루프에 빠지지 않는다.
def recursive_function(i):
  if(i == 10) : return
  print(i,'번째 재귀 함수를 호출합니다.')
  recursive_function(i+1)

recursive_function(1)

# 팩토리얼 구하기
def factorial(n):
  if (n <= 1): 
    return 1
  elif(n > 1):
    return factorial(n-1) * n

print(factorial(4))