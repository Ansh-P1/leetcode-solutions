class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        a = float('inf')
        maxi = 0
        for p in prices:
            if p<a:
                a = p
            else:
                maxi = max(maxi, p-a)
        return maxi
        