'''
349. Intersection of Two Arrays
Solved
Easy
Topics
Companies
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
'''

def intersection(nums1,nums2):
        set_1=set(nums1)
        set_2=set(nums2)
        res=[]
        for num in set_1:
            if num in set_2:
                res.append(num)  
        return res 
    
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
p=intersection(nums1,nums2)
print(p)

'''
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                # Found intersection, add to result and move both pointers
                if not res or res[-1] != nums1[i]:  # Check if the last added element is not the same
                    res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                # nums1[i] is smaller, move pointer i forward
                i += 1
            else:
                # nums2[j] is smaller, move pointer j forward
                j += 1
        
        return res
'''