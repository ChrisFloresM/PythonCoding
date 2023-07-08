# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         result = True
#         for letter in ransomNote:
#             if letter in magazine:
#                 magazine = magazine.replace(letter, "", 1)
#             else:
#                 result = False
            
#         return result
 
#Hash Map approach
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         result = True
#         HashMap = dict.fromkeys(magazine, 0)
        
#         for letter in magazine:
#             HashMap[letter] += 1
            
#         for letter in ransomNote:
#             if letter not in magazine or HashMap[letter] == 0:
#                 return False
#             else:
#                 HashMap[letter] -= 1
            
#         return result       

#Using Counter function    
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        result = True
        HashMap = dict.fromkeys(magazine, 0)
        
        for letter in magazine:
            HashMap[letter] += 1
            
        for letter in ransomNote:
            if letter not in magazine or HashMap[letter] == 0:
                return False
            else:
                HashMap[letter] -= 1
            
        return result       
    
mySolution = Solution()
print(mySolution.canConstruct("a","b"))
print(mySolution.canConstruct("aa","ab"))
print(mySolution.canConstruct("aa","aab"))
