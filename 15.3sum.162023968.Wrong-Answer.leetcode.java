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
            if (i - 1 >= 0 && num[i] == num[i - 1])
            {
                continue;
            }

            int j = i + 1, k = num.length - 1;

            while (j < k)
            {
                if (num[i] + num[j] + num[k] == 0)
                {
                    ArrayList<Integer> temp = new ArrayList<Integer>();
                    temp.add(num[i]);
                    temp.add(num[j]);
                    temp.add(num[k]);
                    result.add(temp);
                    k--;
                    j++;
                }
                else if (num[i] + num[j] + num[k] > 0)
                {
                    k--;
                }
                else
                {
                    j++;
                }
            }
        }

        return result;
    }
}
