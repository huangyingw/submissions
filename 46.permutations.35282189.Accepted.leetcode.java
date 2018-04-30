public class Solution
{
    public List<List<Integer>> permute(int[] num)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        dfs(num, new boolean[num.length], new ArrayList<Integer>(), result);
        return result;
    }

    public void dfs(int[] num, boolean[] visited,
                    List<Integer> current, List<List<Integer>> result)
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
            dfs(num, visited, current, result);
            current.remove(current.size() - 1);
            visited[i] = false;
        }
    }
}

