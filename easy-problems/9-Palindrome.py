class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0): return False
        else:
            v = []
            while(x):
                i=0
                p = int(x%10)
                v.append(p)
                i+=1
                x = int(x/10)
            z = []
            z = v.copy()
            z.reverse()
            return(v == z)
sol = Solution()
result = sol.isPalindrome(121)
print(result)
