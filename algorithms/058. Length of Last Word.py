# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space
# characters only.

# For example,
# Given s = "Hello World",
# return 5.


class Solution(object):

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lastlen = 0
        length = len(s)
        for i in range(length - 1, -1, -1):
            if s[i] == ' ':
                if lastlen == 0:
                    continue
                break
            else:
                lastlen += 1
        return lastlen
