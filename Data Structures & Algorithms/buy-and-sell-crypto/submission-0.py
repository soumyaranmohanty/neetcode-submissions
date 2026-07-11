class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxprofit=[]
        
        for i in range(-1, -len(prices)-1, -1):
            #print(prices[i])
            
            profits=[0]
            profit = 0
            for j in range(i-1, -len(prices)-1, -1):
                if (prices[i]-prices[j])>profit:
                    profit=prices[i]-prices[j]
                
                profits.append(profit)
            #print(profits)
            maxprofit.append(max(profits)) 
        return max(maxprofit)

            