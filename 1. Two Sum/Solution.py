class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[j] + nums[i] == target:
        #             return [i,j]
        
        # Hash Map
        seen = {}
        for i, n in enumerate(nums):
            # print(i,n)
            complement = target - n
            if complement in seen:
                return [seen[complement],i]
            seen[n] = i
            
            

        


        