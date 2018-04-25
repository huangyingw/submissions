public class Solution
{
    public int[] twoSum(final int[] numbers, int target)
    {
        List<Integer> pos = new ArrayList<Integer>();

        for (int i = 0; i < numbers.length; i++)
        {
            pos.add(i);
        }

        Collections.sort(pos, new Comparator<Integer>()
        {
            @Override
            public int compare(Integer o1, Integer o2)
            {
                return numbers[o1] - numbers[o2];
            }
        });
        int i = 0;
        int j = numbers.length - 1;

        while (i < j)
        {
            int sum = numbers[pos.get(i)] + numbers[pos.get(j)];

            if (sum < target)
            {
                i++;
            }
            else if (sum > target)
            {
                j--;
            }
            else
            {
                int[] ans = new int[2];
                ans[0] = Math.min(pos.get(i), pos.get(j)) + 1;
                ans[1] = Math.max(pos.get(i), pos.get(j)) + 1;
                return ans;
            }
        }

        return null;
    }
}

