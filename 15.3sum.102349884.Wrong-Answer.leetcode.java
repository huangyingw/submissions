public class Solution
{
    public List<List<Integer>> threeSum(int[] num)
    {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        if (num.length < 3)
        {
            return res;
        }

        Arrays.sort(num);

        for (int i = 0; i < num.length - 2; i++)
        {
            if (i > 0 && num[i] == num[i - 1])
            {
                continue;
            }

            int j = i + 1, k = num.length - 1;

            while (j < k)
            {
                if (j < k && k < num.length - 1 && num[k] == num[k + 1])
                {
                    k-- ;
                }

                if (j < k && j > i + 1 && num[j] == num[j - 1])
                {
                    j++ ;
                }

                if (num[j] + num[k] + num[i] == 0)
                {
                    ArrayList<Integer> temp = new ArrayList<Integer>();
                    temp.add(num[i]);
                    temp.add(num[j]);
                    temp.add(num[k]);
                    res.add(temp);
                    k-- ;
                    j++ ;
                }
                else if (num[j] + num[k] + num[i] > 0)
                {
                    k-- ;
                }
                else
                {
                    j++ ;
                }
            }
        }

        return res;
    }
}
