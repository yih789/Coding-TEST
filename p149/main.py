from collections import deque

N, M = map(int, input().split())

ice = []
visited = []
for row in range(N):
  ice.append(list(map(int, input().split())))
  visited.append([False]*M)

def bfs(graph, visited):
  queue = deque([graph[0][0]])
  visited[0][0] = True
  for i in range 

