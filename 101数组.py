# strs = ["abca","abc","abca","abc","abcc"]
# for str in strs:
#     for j in range(len(str)):
#         print(str[j])
#         if j == len(str) - 1:
#             print('-'*50)



#
# from typing import List
#
#
# class Solution:
#     def longestCommonPrefix(self , strs: List[str]) -> str:
#         # write code here
#         commonPrefix = strs[0]
#         print(commonPrefix)
#
#         for s in strs[1:]:
#
#             while not s.startswith(commonPrefix):
#                 commonPrefix = commonPrefix[:-1]
#
#         if  commonPrefix is None:
#             return ''
#         return commonPrefix
#
#
#
# Solution().longestCommonPrefix([])



i = '1a1.4.5.6'
print(i.isnumeric())