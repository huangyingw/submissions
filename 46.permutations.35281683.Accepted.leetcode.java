public class Solution
{
    public List<List<Integer>> permute(int[] num)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> current = new ArrayList<Integer>();
        boolean[] visited = new boolean[num.length];
        dfs(num, result, current, visited);
        return result;
    }
    public void dfs(int[] num, List<List<Integer>> result,
                    List<Integer> current, boolean[] visited)
    {
        if (current.size() == num.length)
        {
            result.add(new ArrayList<Integer>(current));
            return;
        }

        for (int i = 0; i < num.length; i++)
        {
            if (visited[i])
            {
                continue;
            }

            visited[i] = true;
            current.add(num[i]);
            dfs(num, result, current, visited);
            current.remove(current.size() - 1);
            visited[i] = false;
        }
    }
}
