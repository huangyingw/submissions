public class Solution
{
    public int longestConsecutive(int[] nums)
    {
        HashSet<Integer> used = new HashSet<Integer>();

        for (int num : nums)
        {
            used.add(num);
        }

        int result = 0;

        for (int num : nums)
        {
            int left = num - 1;

            while (used.contains(left))
            {
                used.remove(left);
                left-- ;
            }

            int right = num + 1;

            while (used.contains(right))
            {
                used.remove(right);
                right++ ;
            }

            result = Math.max(result, right - left - 1);
        }

        return result;
    }
}
