public class Solution
{
    public List<String> generateParenthesis(int n)
    {
        if (n < 0)
        {
            return null;
        }

        List<String> result = new ArrayList<String>();
        dfs(result, "", n, n);
        return result;
    }

    private void dfs(List<String> result, String s, int left, int right)
    {
        if (left > right || left < 0)
        {
            return;
        }

        if (right == 0)
        {
            result.add(s);
        }

        dfs(result, s + "(", left - 1, right);
        dfs(result, s + ")", left, right - 1);
    }
}
