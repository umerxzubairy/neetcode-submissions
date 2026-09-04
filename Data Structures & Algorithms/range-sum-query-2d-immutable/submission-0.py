class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])

        self.matrix = [[0] * (COLS + 1) for _ in range(ROWS+1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix = prefix + matrix[r][c]
                above = self.matrix[r][c+1]
                self.matrix[r+1][c+1] = above+ prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1+1, col1+1, row2+1, col2+1
        right = self.matrix[r2][c2]
        above = self.matrix[r1-1][c2]
        left = self.matrix[r2][c1-1]
        topLeft = self.matrix[r1-1][c1-1]
        return right - above - left + topLeft        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)