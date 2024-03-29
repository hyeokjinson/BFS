import sys

n=int(sys.stdin.readline())

maze=[list(map(int,input()))for _ in range(n)]

def dfs(maze1,cnt,x,y):
    maze1[x][y]=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<n:
            if maze1[nx][ny]==1:
                cnt=dfs(maze1,cnt+1,nx,ny)
    return cnt
ans=[]
for i in range(n):
    for j in range(n):
        if maze[i][j]==1:
            ans.append(dfs(maze,1,i,j))

print(len(ans))
for i in sorted(ans):
    print(i)

