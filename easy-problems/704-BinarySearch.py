class Solution:
    def search(self, nums: list[int], target: int) -> int:
        found = False
        r = len(nums)-1
        l = 0
        while l<=r:
            mid = (l+r)//2
            if(nums[mid] == target):
                found = True
                return mid-1
            if(nums[mid] < target):
                l = mid + 1
            if(nums[mid]> target):
                r = mid-1
        if not found :
            return -1
        
sol = Solution()
result = sol.search([-1,0,3,5,9,12] , 9 )
print(result)