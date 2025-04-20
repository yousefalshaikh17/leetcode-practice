# 20. Valid Parentheses
# Topics: String, Stack
# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        openings = set(['(','{','['])
        closings = set([')','}',']'])

        pairings = {
            '[':']',
            '(':')',
            '{':'}'
        }

        stack = []
        for c in s:
            if c in openings:
                stack.append(c)
            elif c in closings:
                if len(stack) == 0:
                    return False
                if pairings[stack[-1]] != c:
                    return False
                stack.pop(-1)

        if len(stack) > 0:
            return False
        
        return True
