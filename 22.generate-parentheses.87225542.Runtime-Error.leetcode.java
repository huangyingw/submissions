public class Solution
{
    public List<String> generateParenthesis(int n)
    {
        if (n < 0)
        {
            return null;
        }

        List<String> result = new ArrayList<String>();
        dfs(result, new StringBuilder(), n, n);
        return result;
    }
    private void dfs(List<String> result, StringBuilder sb, int left, int right)
    {
        if (left > right)
        {
            return;
        }

        if (left == 0 && right == 0)
        {
            result.add(sb.toString());
            return;
        }

        sb.append("(");
        dfs(result, sb, left - 1, right);
        sb.setLength(sb.length() - 1);
        sb.append(")");
        dfs(result, sb, left, right - 1);
        sb.setLength(sb.length() - 1);
    }
}
