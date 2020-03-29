N,M,G,R=map(int,input().split()) #N,M행과열,G(초록색배양액개수),R(빨간색배양액의개수)
matrix=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
max_value=0
for i in range(N):
    l= list(map(int, input().strip().split()))
    matrix.append(l)

def spread(x,y,matrix):
    while matrix:

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<M and ny>=0 and ny<N:
                if matrix[nx][ny]==0:
                    continue
                if matrix[nx][ny]==1 or matrix[nx][ny]==2:
                    return 1