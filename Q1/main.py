N = map(int, input())

data = list(map(int, input().split()))

# 공포도 오름차순
# 작은 인원으로 많은 그룹 생성을 위해
data.sort()

# 그룹 수
group = 0
# 멤버 수
member = 0

for x in data:
  member += 1
  if member >= x:
    group += 1
    member = 0

print('그룹의 수 :',group)



