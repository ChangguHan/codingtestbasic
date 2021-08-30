"""
아이디어
- 한점에서 다른 모든 점으로의 최단경로 > 다익스트라 사용
- 모든 점 거리 초기값 무한대로 설정
- 시작점 거리 0 설정 및 힙에 추가
- 힙에서 하나씩 빼면서 수행할 것
    - 현재 거리가 새로운 간선 거칠때보다 크다면 갱신
    - 새로운 거리 힙에 추가

시간복잡도
- 다익스트라 시간복잡도 : ElgV
    - E : 3e5, lgV = 20
- O(ElgV) = 6e6 > 가능

자료구조
- 다익스트라 사용 힙 : [(비용, 다음 간선)]
- 거리 배열 : [num]
- 간선, 인접 리스트 : [(비용, 다음 간선)]
"""


import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

V,E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V+1)]
dist = [INF] * (V+1)
heap = []

for i in range(E):
    u,v,w = map(int, input().split())
    edge[u].append((w,v))

dist[K]=0
heapq.heappush(heap, (0,K))

while heap:
    w,v = heapq.heappop(heap)
    if w != dist[v]: continue
    for nw, nv in edge[v]:
        if dist[nv] > dist[v] + nw:
            dist[nv] = dist[v] + nw
            heapq.heappush(heap, (dist[nv], nv))

for i in range(1,V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])