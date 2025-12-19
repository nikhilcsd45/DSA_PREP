def solve(self, board):
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])
        visited = [[0]*cols for _ in range(rows)]
        drow = [-1, 0, 1, 0]
        dcol = [0, 1, 0, -1]

        def dfs(r, c):
            visited[r][c] = 1
            for i in range(4):
                nrow = r + drow[i]
                ncol = c + dcol[i]
                if (0 <= nrow < rows and 0 <= ncol < cols and
                    board[nrow][ncol] == "O" and visited[nrow][ncol] == 0):
                    dfs(nrow, ncol)
    
        # Step 1: Mark all boundary-connected 'O's
        for i in range(cols):
            if board[0][i] == "O" and visited[0][i] == 0:
                dfs(0, i)
            if board[rows-1][i] == "O" and visited[rows-1][i] == 0:
                dfs(rows-1, i)

        for i in range(rows):
            if board[i][0] == "O" and visited[i][0] == 0:
                dfs(i, 0)
            if board[i][cols-1] == "O" and visited[i][cols-1] == 0:
                dfs(i, cols-1)

        # Step 2: Flip all unvisited 'O's to 'X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"

        return board
