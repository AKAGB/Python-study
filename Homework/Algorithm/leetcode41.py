class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for each in nums:
            x |= int(2**each)
        cnt = 1
        x >>= 1
        while x % 2:
            cnt += 1
            x >>= 1
        return cnt

sol = Solution()
print(sol.firstMissingPositive([7, 8, 9, 11, 12]))