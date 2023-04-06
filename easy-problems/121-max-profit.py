class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                profit = prices[i] - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    
sol = Solution()
result = sol.maxProfit([7,6,4,3,1])
print(result)

