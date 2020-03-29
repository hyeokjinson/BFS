from sys import*

def dfs(matrix,cnt,x,y):
    matrix[x][y]=1
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx>=0 and nx<N and ny>=0 and ny<M:
            if matrix[ny][nx]==0:
                dfs(matrix,cnt+1,nx,ny)
    return cnt

M,N,K=map(int,input().split())
matrix=[[0]*N for i in range(M)]
arr=[]
for i in range(K):
    x1,y1,x2,y2=map(int,input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            matrix[j][k]=1

for i in range(M):
    for j in range(M):
        if matrix[i][j]==0:
            arr.append(dfs(matrix,1,i,j))

print(len(arr))
for i in sorted(arr):
    print(i)
