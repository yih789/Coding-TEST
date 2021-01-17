# find_parent
def find_parent(parent, x):
  if(parent[x] != x):
    return find_parent(parent, parent[x])
  return x

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

# 모든 간선에 대해 union연산
for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

# 부모 테이블 내용 출력
print('부모 테이블: ', end=' ')
for i in range(1, v+1):
  print(parent[i], end=' ')

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합: ', end=' ')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print()




