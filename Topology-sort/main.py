from collections import deque

# 노드 개수, 간선 개수
v, e = map(int, input().split())
# 진입 차수 리스트
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보 입력
for i in range(e):
  a, b = map(int, input().split())
  # 연결 정보
  graph[a].append(b)
  # 진입차수 증가
  indegree[b] += 1

# 위상정렬
def topology_sort():
  result = [] # 알고리즘 수행 결과 리스트
  q = deque()

  for i in range(1, v + 1):
    if indegree[i] == 0:
      q.append(i)

  while q: # 큐가 빌 때까지
    now = q.popleft()
    result.append(now)
    for node in graph[now]:
      indegree[node] -= 1
      if indegree[node] == 0:
        q.append(node)

  # 위상정렬 결과 출력
  for i in result:
    print(i, end=' ')

topology_sort()



