import sys
r=sys.stdin.readline
n,m=map(int,sys.stdin.readline().split())

adj=[[] for i in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    a,b=map(int,r().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(v):
    visited[v]=True
    for i in adj[v]:
        if not (visited[i]):
            bfs(i)

cnt=0
for i in range(1,n+1):
    if not(visited[i]):
        cnt+=1
        bfs(i)

print(cnt)