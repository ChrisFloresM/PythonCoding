class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step_count = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            step_count += 1
        return step_count
  
class Solution2(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        step_count = 0
        while num > 0:
            if num & 1:
                num -= 1
            else:
                num = 1
            step_count += 1
        return step_count  
    
mySolution = Solution()
mySolution2 = Solution2()

""" print(mySolution.numberOfSteps(14))
print(mySolution.numberOfSteps(8))
print(mySolution.numberOfSteps(123)) """

print(mySolution2.numberOfSteps(14))
print(mySolution2.numberOfSteps(8))
print(mySolution2.numberOfSteps(123))
        
        