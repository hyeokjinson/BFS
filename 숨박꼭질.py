import sys
from collections import deque

def bfs():
    q=deque()
    q.append(n)
    cnt=0
    while q:
        for _ in range(len(q)):
            v=q.popleft()
            if v==m:
                print(cnt)
                return
            if v*2<MAX and time[v*2]==0:
                q.append(v*2)
                time[v*2]=time[v]+1


            if v+1<MAX and time[v+1]==0:
                q.append(v+1)
                time[v+1]=time[v]+1

            if v-1>=0 and time[v-1]==0:
                q.append(v-1)
                time[v-1]=time[v]+1

        cnt+=1

n,m=map(int,input().split())
MAX=100001
time=[0]*MAX
bfs()
