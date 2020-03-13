from collections import deque
import sys
input=sys.stdin.readline

n=int(input())
x,y=map(int,input().split())
a=[[] for i in range(n+1)]
dist=[0 for _ in range(n+1)]
for _ in range(int(input())):
    u,v=map(int,input().split())
    a[u].append(v)
    a[v].append(u)

def bfs():
    q=deque()
    q.append(x)
    while q:
        now=q.popleft()
        if now ==y:
            return dist[now]
        for i in a[now]:
            if dist[i]==0:
                q.append(i)
                dist[i]=dist[now]+1
    return -1
print(bfs())