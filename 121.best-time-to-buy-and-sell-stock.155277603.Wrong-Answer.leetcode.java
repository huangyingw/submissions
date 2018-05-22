public class Solution
{
    public int maxProfit(int[] prices)
    {
        if (prices == null || prices.length < 2)
        {
            return 0;
        }

        int minPrice = Integer.MAX_VALUE;
        int maxProf = Integer.MIN_VALUE;

        for (int i = 1; i < prices.length; i++)
        {
            minPrice = Math.min(minPrice, prices[i - 1]);
            maxProf = Math.max(maxProf, prices[i] - minPrice);
        }

        return maxProf;
    }
}

