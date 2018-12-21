<<< <<< < Updated upstream
public class Solution
{
    public int longestConsecutive(int[] nums)
    {
        int result = 1;
        Set<Integer> dict = new HashSet<Integer>();

        for (int num : nums)
        {
            dict.add(num);
        }

        for (int num : nums)
        {
            int count = 1;

            if (dict.contains(num))
            {
                int right = num + 1;
                == == == =
                    public class Solution
                {
                    public int longestConsecutive(int[] nums)
                    {
                        int result = 1;
                        Set<Integer> dict = new HashSet<Integer>();

                        for (int num : nums)
                        {
                            dict.add(num);
                        }

                        for (int num : nums)
                        {
                            int count = 1;

                            if (dict.contains(num))
                            {
                                int right = num + 1;
                                >>> >>> > Stashed changes

                                while (dict.contains(right))
                                {
                                    count++;
                                    dict.remove(right++);
                                }

                                <<< <<< < Updated upstream
                                int left = num - 1;
                                == == == =
                                    int left = num - 1;
                                >>> >>> > Stashed changes

                                while (dict.contains(left))
                                {
                                    count++;
                                    dict.remove(left--);
                                }

                                <<< <<< < Updated upstream
                                dict.remove(num);
                            }

                            result = Math.max(result, count);
                        }

                        == == == =
                            dict.remove(num);
                    }

                    result = Math.max(result, count);
                }
                >>> >>> > Stashed changes
                return result;
            }
        }