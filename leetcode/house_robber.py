# You are a professional robber planning to rob houses along a street. Each 
# house has a certain amount of money stashed, the only constraint stopping you 
# from robbing each of them is that adjacent houses have security system 
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of 
# each house, determine the maximum amount of money you can rob tonight 
# without alerting the police.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        steal, not_steal = 0, 0
        for num in nums:
            steal, not_steal = not_steal + num, max(steal, not_steal)
        return max(steal, not_steal)

if __name__ == "__main__":
    solution = Solution()
    print solution.rob([1, 2, 3, 1])
