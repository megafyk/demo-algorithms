class Solution(object):
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return []
        else:
            return [s[-1]] + self.reverseString(s[:-1])