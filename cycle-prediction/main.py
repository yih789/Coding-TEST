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

cycle = False

# 모든 간선에 대해 union연산
for i in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)

if cycle:
  print('사이클이 발생했습니다.')
else:
  print('사이클이 발생하지 않았습니다.')
