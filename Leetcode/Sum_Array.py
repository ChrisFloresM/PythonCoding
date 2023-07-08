class Solution(object):
    def runningSum(self, nums):
        for n in range(1, len(nums)):
            nums[n] = nums[n-1]
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """

my_list = [1, 2, 3, 4, 5]
print(Solution.runningSum(my_list))