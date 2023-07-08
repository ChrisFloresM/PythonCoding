class Solution(object):
    
    def fizzBuzz(self, n):
        outputList = []
        for i in range(1, n+1):
            result = ""
            if i % 3 == 0:
                result += "Fizz"
            if i % 5 == 0:
                result += "Buzz"
            outputList.append(i if not result else result)
                   
        return outputList       
            
                
                
        """
        :type n: int
        :rtype: List[str]
        """
        
        
mySolution = Solution()

mySolution.fizzBuzz(15)