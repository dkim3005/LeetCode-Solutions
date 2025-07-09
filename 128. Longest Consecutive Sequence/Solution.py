class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        longest = 0
        for n in set_nums:
            if n-1 not in set_nums:
                length = 1
                while n + length in set_nums:
                    length += 1
                longest = max(longest, length)
                
        return longest

        