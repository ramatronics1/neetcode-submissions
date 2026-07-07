class Solution:
    def isValid(self, s: str) -> bool:
        openClose = {")":"(", "]":"[", "}":"{"}
        stk = []

        for i in s:
            if i in openClose:
                if stk and stk[-1] == openClose[i]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(i)

        return True if not stk else False                 


        