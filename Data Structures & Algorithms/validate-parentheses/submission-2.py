class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        strmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for char in s:
            if char in strmap:
                if not stack:
                    return False
                top = stack.pop()
                if top != strmap[char]:
                    return False
            else:
                stack.append(char)
        return not stack