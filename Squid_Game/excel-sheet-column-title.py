# https://leetcode.com/problems/excel-sheet-column-title/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            ans += chr( 65 + ((columnNumber - 1) % 26))
            columnNumber = (columnNumber - 1) // 26
        ans = ans[::-1]
        return ans
