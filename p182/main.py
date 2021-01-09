N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

#  A 오름차순
A.sort()
# B 내림차순
B.sort(reverse=True)

# K번 바꿔치기
for i in range(K):
  # A와 B가 같거나 A가 더 크면 바뀌치기 중단
  if(A[i] >= B[i]):
    break
  A[i], B[i] = B[i], A[i]

print(sum(A))
