public class Solution
{
    // [0,1,2,4,5,7], return ["0->2","4->5","7"].
    public List<String> summaryRanges(int[] nums)
    {
        List<String> result = new ArrayList<>();

        if (nums == null || nums.length < 1)
        {
            return  result;
        }

        int s = 0, e = 0;

        while (e < nums.length)
        {
            if (e + 1 < nums.length && nums[e + 1] == nums[e] + 1)
            {
                e++;
            }
            else
            {
                if (s == e)
                {
                    result.add(Integer.toString(nums[s]));
                }
                else
                {
                    String str = nums[s] + "->" + nums[e];
                    result.add(str);
                }

                ++e;
                s = e;
            }
        }

        return result;
    }
}
