from collections import deque
def updateMatrix(self, mat):
    rows=len(mat)
    cols=len(mat[0])
    # visited=[[0]*cols for _ in range(rows)]
    dis=[[-1]*cols for _ in range(rows)]
    q=deque()
    for i in range(rows):
        for j in range(cols):
            if mat[i][j]==0:
                q.append((i,j,0))
                # visited[i][j]=1
                dis[i][j]=0

    drow=[-1,0,1,0]
    dcol=[0,1,0,-1]
    while q:
        r,c,d=q.popleft()
        for i in range(4):
            nrow=r+drow[i]
            ncol=c+dcol[i]
            if (0<=nrow<rows) and (0<=ncol<cols) and dis[nrow][ncol]==-1:
                # visited[nrow][ncol]=1

                dis[nrow][ncol]=d+1
                q.append((nrow,ncol,d+1))
    return dis



    