import sys
import copy
r=sys.stdin.readline

n,k=map(int,r().split())
maze=[]
for i in range(n):
    l=list(map(int,input().strip().split()))
    maze.append(l)
dx=[-1,0,1,0]
dy=[0,1,0,-1]
max_value=0

def select_wall(start,count):
    global max_value
    if count==3:
        sel_nm=copy.deepcopy(maze)
        for i in range(n):
            for j in range(k):
                spread_virus(i,j,sel_nm)
        safe_counts=sum(i.count(0)for i in sel_nm)
        max_value=(max_value,safe_counts)
        return True

    else:
        for i in range(start,n*k):
            r=i//k
            c=i%k
            if maze[r][c]==0:
                maze[r][c]=1
                select_wall(i,count+1)
                maze[r][c]=0


def spread_virus(x,y,sel_nm):
    if sel_nm[x][y]==2:

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and ny>=0 and nx<n and ny<k:
                if sel_nm[nx][ny]==0:
                    sel_nm[nx][ny]=2
                    spread_virus(nx,ny,sel_nm)

select_wall(0,0)
print(max_value)