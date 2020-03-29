import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())
dist = [[0]*m for _ in range(n)]
a = []
for _ in range(n):
    a.append(sys.stdin.readline())

def bfs():
    q = [(0, 0)]
    dist[0][0] = 1
    while q:
        x, y = q.pop(0)
        if x == n-1 and y == m-1:
            print(dist[x][y])
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if dist[nx][ny] > 0 or a[nx][ny] == '0':
                continue
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

bfs()

