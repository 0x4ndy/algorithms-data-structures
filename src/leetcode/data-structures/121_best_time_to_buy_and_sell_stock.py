"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

import sys
from typing import List


class Solution:
    def max_profit1(self, prices: List[int]) -> int:
        # Brute force - not accepted on leetcode
        max_profit = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

    def max_profit2(self, prices: List[int]) -> int:
        # Single pass O(n) - looking for min  followed by max
        minprice = sys.maxsize
        maxprofit = 0
        for n in prices:
            if n < minprice:
                minprice = n
            elif n - minprice > maxprofit:
                maxprofit = n - minprice

        return maxprofit
