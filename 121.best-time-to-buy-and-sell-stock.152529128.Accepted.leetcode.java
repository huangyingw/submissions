public class Solution
{
    public int maxProfit(int[] prices)
    {
        int maxProfit = 0;

        if (prices == null | prices.length == 0)
        {
            return maxProfit;
        }

        int minPrice = prices[0];

        for (int i = 1; i < prices.length; i++)
        {
            minPrice = Math.min(minPrice, prices[i - 1]);
            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
}

