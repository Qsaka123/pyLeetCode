# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = []
        while n != 0:
            res.insert(0, chr((n - 1) % 26 + 65))
            n = (n - 1) / 26
        return ''.join(res)
