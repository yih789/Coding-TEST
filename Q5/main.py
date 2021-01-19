# 공의 개수, 최대 무게
N, M = map(int, input().split())

weight = list(map(int, input().split()))
# 중복성 제거
set_w = set(weight)

# 경우의 수
result = 0
# 지나온 무게의 총합
temp = 0

# 순서대로 해당 무게를 고를 경우의 수 구하기
for w in set_w:
  temp += weight.count(w)
  # 해당 무게 개수 * 전체-(1~해당)무게 개수
  result += weight.count(w) * (N - temp) 
  
print(result)