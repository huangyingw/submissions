public class Solution
{

    public ArrayList<ArrayList<Integer>> combinationSum2(int[] num,
            int target)
    {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();

        if (num == null || num.length == 0)
        {
            return res;
        }

        Arrays.sort(num);
        helper(num, 0, target, new ArrayList<Integer>(), res);
        return res;
    }

    private void helper(int[] num, int start, int target,
                        ArrayList<Integer> current,
                        ArrayList<ArrayList<Integer>> res)
    {
        if (target == 0)
        {
            res.add(new ArrayList<Integer>(current));
            return;
        }

        if (target < 0 || start >= num.length)
        {
            return;
        }

        for (int index = start; index < num.length; index++)
        {
            if (index > start && num[index] == num[index - 1])
            {
                continue;
            }

            current.add(num[index]);
            helper(num, index + 1, target - num[index], current, res);
            current.remove(current.size() - 1);
        }
    }
}

