#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, r, c, word, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or \
           r >= len(board) or c >= len(board[0]) or \
           word[index] != board[r][c]:
            return False

        board[r][c] = "#"
        found = self.dfs(board, r+1, c, word, index+1) or \
                self.dfs(board, r-1, c, word, index+1) or \
                self.dfs(board, r, c+1, word, index+1) or \
                self.dfs(board, r, c-1, word, index+1)
        board[r][c] = word[index]
        
        return found
        
# @lc code=end

