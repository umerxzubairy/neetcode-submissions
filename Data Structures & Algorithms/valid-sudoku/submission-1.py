class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        dic = defaultdict(set)
        rdic = defaultdict(set)
        cdic = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rdic[r] or val in cdic[c] or val in dic[(r//3, c//3)]:
                    return False
                rdic[r].add(val)
                cdic[c].add(val)
                dic[(r//3, c//3)].add(val)
        return True