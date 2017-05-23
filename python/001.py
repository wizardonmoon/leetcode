class Solution(object):

    def twoSum(self, nums, target):

        """

        :type nums: List[int]

        :type target: int

        :rtype: List[int]

        """

        minus_nums = [target - n for n in nums]

        minus_nums.reverse()

        minus_set = set(minus_nums)

        for i in range(len(nums)):

            if nums[i] in minus_set:

                curr_idx = i

                other_idx = minus_nums.index(nums[i])

                if curr_idx + other_idx != len(nums) - 1:

                    return [curr_idx, len(nums) - 1 - other_idx]
