'''
3046. Split the Array
Easy
Topics
Companies
Hint
You are given an integer array nums of even length. You have to split the array into two parts nums1 and nums2 such that:

nums1.length == nums2.length == nums.length / 2.
nums1 should contain distinct elements.
nums2 should also contain distinct elements.
Return true if it is possible to split the array, and false otherwise.

Example 1:

Input: nums = [1,1,2,2,3,4]
Output: true
Explanation: One of the possible ways to split nums is nums1 = [1,2,3] and nums2 = [1,2,4].
Example 2:

Input: nums = [1,1,1,1]
Output: false
Explanation: The only possible way to split nums is nums1 = [1,1] and nums2 = [1,1]. Both nums1 and nums2 do not contain distinct elements. Therefore, we return false.
'''

# wrong......
# def split(nums):
#         nums.sort()
#         n1=[]
#         n2=[]
#         for i in range(0,len(nums)-1,2):
                 
#             if nums[i]!=n1[len(n1)-1] or nums[i]!=n2[len(n2)-1] or n1==[] or n2==[]:
#                 return 'true'
#             n1.append(nums[i])
#             n2.append(nums[i+1])
#         return 'false'
# nums=[1,1,2,2,3,4]
# p=split(nums)
# print(p)

def splitarray(nums):
    freq=[0]*101
    
    for num in nums:
        freq[num]+=1
        if freq[num]>2:
            return False
    return True

nums=[1,1,2,2,3,4]
p=splitarray(nums)
print(p)