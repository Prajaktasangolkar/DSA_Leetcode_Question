'''
1636. Sort Array by Increasing Frequency
Easy
Topics
Companies
Hint
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
'''

def sortarray(nums):
    # freq=[0]*101
    # for i in nums:
    #     freq[i]+=1
    #     if freq[i]>2:
    #         print(i)
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Convert the dictionary to a list of tuples and sort based on the criteria
    sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
    
    return sorted_nums
        
'''
If two elements had the same frequency, the sorting by -x would ensure that the larger number appears before the smaller one. For instance, if nums contained 4 and 5 both with frequency 1, 5 would come before 4.
'''
 
nums = [1,1,2,2,2,3]   
p=sortarray(nums)
print(p)