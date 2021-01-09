N = int(input())

data = []

for i in range(N):
  data.append(int(input()))

# 파이썬 리스트 객체 기본정렬 사용
data.sort(reverse=True)
print(data)