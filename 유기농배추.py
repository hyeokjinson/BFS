import sys
sys.setrecursionlimit(50000)
T=int(input())

def dfs(mat,cnt,x,y):
    mat[x][y]=0
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<M and ny>=0 and ny<N:
            if mat[nx][ny]==1:
                cnt=dfs(mat,cnt+1,nx,ny)
    return cnt
def solve():
    count=0
    for i in range(M):
        for j in range(N):
            if matrix[i][j]==1:
                dfs(matrix,1,i,j)
                count+=1
    return count
arr=[]
for _ in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * N for _ in range(M)]
    for _ in range(K):
        link=list(map(int,input().split()))
        matrix[link[0]][link[1]]=1

    arr.append(solve())

for i in arr:
    print(i)