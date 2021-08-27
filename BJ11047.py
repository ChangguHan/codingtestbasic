"""
1. 아이디어
- 동전을 저장한뒤, 반대로 뒤집음
- 동전 for >
    - 동전 사용개수 추가
    - 동전 사용한만큼 K값 갱신

2. 시간복잡도
- O(N)

3. 자료구조
- 동전 금액 : int[]
- 동전 사용 cnt : int
- 남은 금액 : int
"""

import sys
input = sys.stdin.readline

N,K = map(int, input().split())
coins = [ int(input()) for _ in range(N)]
coins.reverse()
cnt = 0

for each_coin in coins:
    cnt += K // each_coin
    K = K % each_coin

print(cnt)
