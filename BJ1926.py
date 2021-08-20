"""
1. 아이디어
- BFS로 이어진 점들을 확인
- 한번 지나간 점 표시해서 다시 지나가지 않도록함

2. 시간복잡도
- BFS : O(V+E)
- V : 500
- E : 500 * 4
- V+E : 2500 > 가능

3. 자료구조
- 전체 지도 : int [][]
      - 최대 1, int 가능
- 지나갔는지 여부 : boolean [][]

"""

import sys
input = sys.stdin.readline
n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x) :
      ecnt = 1
      q = [(y, x)]
      while q :
            ey, ex = q.pop()
            for k in range(4) :
                  ny, nx = ey + dy[k], ex + dx[k]
                  if 0 <= ny < n and 0 <= nx < m :
                        if map[ny][nx] == 1 and chk[ny][nx] == 0 :
                              ecnt += 1
                              chk[ny][nx] = 1
                              q.append((ny, nx))
      return ecnt

cnt, maxv = 0,0
for j in range(n) :
      for i in range(m) :
            if map[j][i] == 1 and chk[j][i] == False :
                  cnt += 1
                  chk[j][i] = True
                  maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)



