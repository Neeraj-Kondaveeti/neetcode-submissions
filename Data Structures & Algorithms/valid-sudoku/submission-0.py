class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = [set() for _ in range(9)]
        cset = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue

                if value in rset[r]:
                    return False
                rset[r].add(value)

                if value in cset[c]:
                    return False
                cset[c].add(value)

                box_index = (r//3) * 3 + (c//3)
                if value in boxes[box_index]:
                    return False
                boxes[box_index].add(value)

        return True
