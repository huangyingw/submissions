public class Solution
{
    public List<List<Integer>> threeSum(int[] num)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        if (num.length < 3)
        {
            return result;
        }

        Arrays.sort(num);

        for (int i = 0; i + 2 < num.length; i++)
        {
            if (i > 0 && num[i] == num[i - 1])
            {
                continue;
            }

            Set<Integer> set = new HashSet<Integer>();

            for (int j = i + 1; j + 1 < num.length; j++)
            {
                if (set.contains(-num[i] - num[j]))
                {
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(num[i]);
                    temp.add(num[j]);
                    temp.add(-num[i] - num[j]);
                    result.add(temp);
                }
                else
                {
                    set.add(num[i] + num[j]);
                }
            }
        }

        return result;
    }
}
