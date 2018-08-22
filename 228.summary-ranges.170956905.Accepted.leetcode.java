public class Solution
{
    public List<String> summaryRanges(int[] nums)
    {
        List<String> result = new ArrayList<String>();

        for (int start = 0, end = 0; end < nums.length; end++, start = end)
        {
            while (end + 1 < nums.length && nums[end + 1] == nums[end] + 1)
            {
                end++;
            }

            result.add(start == end ? Integer.toString(nums[start]) : nums[start] + "->" + nums[end]);
        }

        return result;
    }
}
