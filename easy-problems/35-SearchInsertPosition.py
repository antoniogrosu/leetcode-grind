class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        r = len(nums)
        l=0
        while(l<=r):
            mid = (l+r)//2
            if():
                return mid+1
            if((nums[mid] < target) and not(nums[mid+1]>target)):
                l = mid + 1
            if((nums[mid]> target) and not(nums[mid-1]<target)):
                r = mid-1

sol = Solution()
result = sol.searchInsert([1,3,5,6] , 5 )
print(result)