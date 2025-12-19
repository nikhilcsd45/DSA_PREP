
def maximalSquare(self, matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        if matrix[i][0] == '1':
            dp[i][0] = 1
            max_side = max(max_side, 1)

    for j in range(cols):
        if matrix[0][j] == '1':
            dp[0][j] = 1
            max_side = max(max_side, 1)

    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == '1':
                dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
                if dp[i][j] > max_side:
                    max_side = dp[i][j]
            else:
                dp[i][j] = 0

    return max_side * max_side
