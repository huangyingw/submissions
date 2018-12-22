public class Solution
{
    public List<List<Integer>> permute(int[] num)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(num, new ArrayList<Integer>(), result);
        return result;
    }

    public void dfs(int[] num, List<Integer> current, List<List<Integer>> result)
    {
        if (current.size() == num.length)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int idx = 0; idx < num.length; idx++)
        {
            if (current.contains(num[idx]))
            {
                continue;
            }

            System.out.printf("idx --> %s\n", idx);
            current.add(num[idx]);
            System.out.printf("current.add --> %s\n", current);
            dfs(num, current, result);
            current.remove(current.size() - 1);
            System.out.printf("current.remove --> %s\n", current);
        }
    }
}
