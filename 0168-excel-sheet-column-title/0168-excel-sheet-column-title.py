class Solution(object):
    def convertToTitle(self, columnNumber):
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            character = chr(ord("A") + (columnNumber % 26))
            result.append(character)
            columnNumber //= 26

        return "".join(reversed(result))