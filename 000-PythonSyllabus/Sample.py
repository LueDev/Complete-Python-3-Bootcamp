from re import L
from typing import List
import cProfile, sys

############## Two Sum 
# class Solution:
#     
# d = {}
# for i, j in enumerate(nums):
#     r = target - j
#     if r in d: return [d[r], i]
#     d[j] = i
# # 
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         idx = 1
#         for _ in nums:
#             j = 0
#             nums2 = nums[idx:]
#             for _ in nums2:
#                 if nums[i] + nums2[j] == target:
#                     j += idx
#                     return [i, j]
#                 else:
#                     j += 1
#             i += 1
#             idx += 1
#         return "no solution"
        
################ isPalindrome 
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         numChar = [num for num in str(x)]
#         print(f"normal: {numChar}\nreversed: {numChar[::-1]}")
#         if numChar == numChar[::-1]:
#             return True
#         else:
#             return False

########### 
# def lookahead(iterable):
#     """Pass through all values from the given iterable, augmented by the
#     information if there are more values to come after the current one
#     (True), or if it is the last value (False).
#     """
#     # Get an iterator and pull the first value.
#     it = iter(iterable)
#     last = next(it)
#     # Run the iterator to exhaustion (starting from the second value).
#     for val in it:
#         # Report the *previous* value (more to come).
#         yield last, True
#         last = val
#     # Report the last value.
#     yield last, False
# print(sys.getsizeof(lookahead(range(100))))
# cProfile.run('lookahead(range(100))')

############## Roman to Int
# class Solution:
#     def romanToIntGen(self, s: str) -> int:
#         roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         prev_value = 0
        
#         for symbol in reversed(s):
#             value = roman_values[symbol]
#             if value < prev_value:
#                 yield -value
#             else:
#                 yield value
#             prev_value = value

# def roman_to_int2(roman: str):
#     s = Solution()
#     return sum(s.romanToIntGen(roman))
        
# sh = roman_to_int2("IIX")  
# print(sh)      
# print(sys.getsizeof(sh))     
        

############## Longest Prefix
# class Solution:
    # def longestCommonPrefix(strs: List[str]) -> str:
       
    #     #Simple solution by abdullayevakbar0101 on leetcode
    #     v = strs
    #     ans=""
    #     v=sorted(v)
    #     first=v[0]
    #     last=v[-1]
    #     for i in range(min(len(first),len(last))):
    #         if(first[i]!=last[i]):
    #             return ans
    #         ans+=first[i]
    #     return ans 
       
       
    #     #The approach should be to create an array with all chars of the first strs element
    #     #Then traverse the rest of the array comparing against the first array
        
    #     prefix = ''
    #     firstElement = [char for char in strs[0]]
    #     smallestElement = len(firstElement)
    #     substr = ''

    #     #If first word's empty, return the empty prefix
    #     if firstElement == "":
    #         return prefix
      
    #     # For single strings, return the whole string
    #     if len(strs) == 1: 
    #         for char in firstElement:
    #             prefix += char
    #         return prefix

    #     # After clearing the edge cases, find the actual prefix 
    #     firstComparisonFlag = True
        
    #     for j in strs[1:]: 
    #         if smallestElement > len(j):
    #             smallestElement = len(j)
    #         for k in range(len(j)):
    #             try:
    #                 if firstElement[k] == j[k]: 
    #                     prefix += j[k] 
    #                     firstComparisonFlag = False
    #                 elif firstElement[k] != j[k] and firstComparisonFlag: 
    #                     return prefix
    #             except IndexError:
    #                 break
        
    #     prefixArr = [char for char in prefix]
        
    #     #Compare prefix against all words to ensure any overly gathered letters are sliced out
    #     for j in strs: 
    #         for k in range(len(j)):
    #             try:
    #                 if prefixArr[k] != j[k]:
    #                     prefix = prefix[:k]
    #             except IndexError:
    #                 break
        
    #     #Confirm size of prefix is not bigger than the smallest element
    #     lengthCheck = prefix[:smallestElement]
    #     prefix = lengthCheck
    #     return prefix
 
 
################## 
   
# s = Solution.longestCommonPrefix(["aac","acab","aa","abba","aa"])     
# print(s)

# myStr = "I am PFB. I provide free python tutorials for you to learn python."
# substring = "python"
# output_string = myStr.replace(substring, "")
# print("The input string is:", myStr)
# print("The substring is:", substring)
# print("The output string is:", output_string)