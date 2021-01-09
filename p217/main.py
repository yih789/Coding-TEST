# x를 5의 배수로 만든다.
# x를 3의 배수로 만든다.
# x를 2의 배수로 만든다.
# 위의 순서가 우선순위 큰 수로 나눌수록 크게 감소

X = int(input())

count = 0

while(X > 1): 
  if X%5 == 0 :
    X /= 5
    count += 1
  elif X%3 == 0 :
    
    X /= 3
    count += 1
  elif X%2 == 0 :
    X /= 2
    count += 1
  else :
    X -= 1
    count += 1

print(count)

