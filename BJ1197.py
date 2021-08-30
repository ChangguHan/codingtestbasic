"""
1. 아이디어
- MST 기본문제, 외우기
- 간선을 인접리스트에 집어넣기
- 힙에 시작점넣기
- 힙이 빌때까지 다음의 작업을 반복
    - 힙의 최소값 꺼내서, 해당 노드 방문 안했다면
            - 방분표시, 해당 비용 추가, 연결된 간선들 힙에 넣어주기

2. 시간복잡도
- MST : O(ElgE)

3. 자료구조
- 간선 저장 되는 인접리스트 : (무게, 노드번호)
- 힙 : (무게, 노드번호)
- 방문 여부 : bool[]
- MST 결과값 : int
"""

import sys
import heapq
input = sys.stdin.readline

V,E = map(int, input().split())
edge = [[] for _ in range(V+1)]
chk = [False] * (V+1)
rs = 0
for i in range(E):
    a,b,c = map(int, input().split())
    edge[a].append([c,b])
    edge[b].append([c, a])

heap = [[0,1]]

while heap:
    w, each_node = heapq.heappop(heap)
    if chk[each_node] == False:
        chk[each_node] = True
        rs += w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]] == False:
                heapq.heappush(heap, next_edge)

print(rs)



