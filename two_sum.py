# file: two_sum.py
# author: Cedric Wille cwille97@bu.edu
# description LeetCode Two Sum working solution
# dat: 2/23/20

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} # hash table
        for i in nums:
            difference = target - i
            if difference in dict:
                return dict.get(difference), nums.index(i)
            dict[i] = nums.index(i)
