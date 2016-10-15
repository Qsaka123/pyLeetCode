# Given a positive integer num, write a function which returns True if num
# is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Returns: True

# Example 2:

# Input: 14
# Returns: False


class Solution(object):

    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in xrange(1, num + 1):
            temp = i**2
            if temp > num:
                break
            if temp == num:
                return True
        return False
