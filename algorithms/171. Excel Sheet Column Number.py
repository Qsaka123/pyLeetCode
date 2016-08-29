# Related to question Excel Sheet Column Title

# Given a column title as appear in an Excel sheet, return its
# corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28


class Solution(object):

    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for index, value in enumerate(s[::-1]):
            res += (ord(value) - 64) * 26**index
        return res
