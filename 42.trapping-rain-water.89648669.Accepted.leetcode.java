public class Solution
{
    public int trap(int[] heights)
    {
        if (heights.length == 0)
        {
            return 0;
        }

        int[] maxHeights = new int[heights.length];
        maxHeights[0] = 0;

        for (int i = 1; i < heights.length; i++)
        {
            maxHeights[i] = Math.max(maxHeights[i - 1], heights[i - 1]);
        }

        int max = 0, area = 0;

        for (int i = heights.length - 2; i >= 0; i--)
        {
            max = Math.max(max, heights[i + 1]);
            area += Math.max(Math.min(max, maxHeights[i]) - heights[i], 0);
        }

        return area;
    }
}
