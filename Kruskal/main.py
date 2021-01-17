# find_parent
def find_parent(parent, x):
  if(parent[x] != x):
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# union_parent
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 노드와 간선 개수 입력
v, e = map(int, input().split())

parent = []
# 부모 테이블, 자기 자신으로 초기화
for i in range(v+1):
  parent.append(i)

# 간선 정보
edges = []
# 총 비용
result = 0

# 모든 간선 정보 얻기
for i in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

# 비용을 기준으로 오름차순 정렬
edges.sort()

# 비용이 작은 간선부터 사이클 확인
for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)
