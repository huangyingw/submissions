public class Solution
{
    public int longestConsecutive(int[] num)
    {
        HashSet<Integer> nums = new HashSet<Integer>();

        for (int n : num)
        {
            nums.add(n);
        }

        int ans = 0;

        for (int n : num)
        {
            int left = n - 1;

            while (nums.contains(left))
            {
                nums.remove(left);
                left--;
            }

            int right = n + 1;

            while (nums.contains(right))
            {
                nums.remove(right);
                right++;
            }

            ans = Math.max(ans, right - left - 1);
        }

        return ans;
    }
}
