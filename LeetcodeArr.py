"""
given list of numbers, need to print out length of list
"""

numbers = [123, 4562, 6654, 4443]
length = len(numbers)
print(length)
y = 2

#2239 Find closest num to zero
nums = [-4, -2, 1, 4, 8]
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int: #O(1n)
        closest = nums[0] #defining varaible
        for x in nums: #loop array
            if abs(x) < abs(closest): #find closest num
                closest = x #closest of closest

        if closest < 0 and abs(closest) in nums: #negative and vositive value in array #O(1n)
            return abs(closest)
        else:
            return closest   # if false closest    

    # time: O(n)= O(2n)
    # space: O(1)  

#13 Roman Integer
input: s = "III"
input: s = "LVIII"
input: s = "MCMXCIV"
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        summ = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                sum += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1

        return summ
    # time: O(n)
    # space O(1)

#392 Is Subsequence
# S = acf => comparing i to each character
# T = abcdef =>>

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S = len(s)
        T = len(t)

        if s == '': return True
        if S > T: return False

        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1

        return False
        #Time: O(T)
        #Space: O(1)
    