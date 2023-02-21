class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        a = [0] * 100000
        for x in nums:
            a[x] += 1
        for x in range(0, len(a)):
            if a[x] == 1:
                return(x)