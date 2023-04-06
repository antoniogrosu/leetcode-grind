class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        new_nums = []
        for i in range(len(nums)):
            if not nums[i] in new_nums:
                new_nums.append(nums[i])
        elem_sum = 0
        for i in range(len(nums)):
            elem_sum += nums[i]
        max_sum = 0
        for i in range(len(new_nums)):
            max_sum += 2 * new_nums[i]
        return (max_sum - elem_sum)




sol = Solution()
result = sol.singleNumber([-1,-1,-2])
print(result)
