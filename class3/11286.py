import heapq
import sys
N = int(sys.stdin.readline())
heap = [] 
for i in range(N):
  num = int(stdin.readline())
  if num == 0:
    if heap:
      print(heapq.heappop(heap)[1])
    else:
      print(0)
  else:
    heapq.heappush(heap, [abs(num), num]) # 절댓값 처리해 작은 값부터 힙에 넣는다.(우선순위, 값)
