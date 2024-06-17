'''633. Sum of Square Numbers
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false'''
import math
def judgeSquareSum(c) :
        left=0
        right=c
        while left <= right:
            current_sum = left * left + right * right
            if current_sum == c or (left*left)==c:
                return True
            elif current_sum < c:
                left += 1
            else:
                right -= 1
        return False
    
c=4
p=judgeSquareSum(c)   
print(p)
print(int(math.sqrt(4)))
