'''
896. Monotonic Array
Solved
Easy
Topics
Companies
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
'''


def array(nums):
    for i in range(1,len(nums)-1):
            if nums[i]>=nums[i+1] and nums[i]<=nums[i-1]:
                return 'true'
            
    return 'false'

nums=[1,3,2]
p=array(nums)
print(p)


# return nums==sorted(nums) or nums==sorted(nums,reverse=True)