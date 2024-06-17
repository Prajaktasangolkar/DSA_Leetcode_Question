'''
1929. Concatenation of Array
Easy
Topics
Companies
Hint
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
Example 2:

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
'''

"""array1 = [1, 2, 3];
array2 = [4, 5, 6];

# // Concatenate the arrays using the spread operator

concatenatedArray = array1.extend(array2)
c1=array1+array2
c2=[*array1,*array2]

print(concatenatedArray);
print(c1);
print(c2);

if want unique concate do list(set(array1,array2))

"""

a={1,2,4,'hi'}
b=list(a)
print(type(b))
print(b)
a=[1,2,3]
b=[3,4,5]
c=list(set(a+b))
print(type(c))

def concate(nums):
    return nums+nums

nums=[1,2,3,4]
p=concate(nums)
print(p)