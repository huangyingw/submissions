public class Solution
{
    public List<String> summaryRanges(int[] nums)
    {
        List<String> res = new ArrayList<String>();

        if (nums == null || nums.length < 1)
        {
            return res;
        }

        int start = 0;
        
        for (int end = 0; end < nums.length; end++)
        {
            start = end;
            
            while (end + 1 < nums.length && nums[end + 1] == nums[end] + 1)
            {
                end++ ;
            }

            if (start == end)
            {
                res.add(Integer.toString(nums[start]));
            }
            else
            {
                String str = nums[start] + "->" + nums[end];
                res.add(str);
            }
        }

        return res;
    }
}
