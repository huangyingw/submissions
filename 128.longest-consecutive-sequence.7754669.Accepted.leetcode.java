public class Solution
{
    public int longestConsecutive(int[] num)
    {
        HashSet<Integer> usded = new HashSet<Integer>();

        for (int n : num)
        {
            usded.add(n);
        }

        int ans = 0;

        for (int n : num)
        {
            int left = n - 1;

            while (usded.contains(left))
            {
                usded.remove(left);
                left--;
            }

            int right = n + 1;

            while (usded.contains(right))
            {
                usded.remove(right);
                right++;
            }

            ans = Math.max(ans, right - left - 1);
        }

        return ans;
    }
}

