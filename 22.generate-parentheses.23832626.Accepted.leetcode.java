public class Solution
{
    public List<String> generateParenthesis(int n)
    {
        if (n < 0)
        {
            return null;
        }

        List<String> result = new ArrayList<String>();
        helper(result, new StringBuilder(), n, n);
        return result;
    }

    private void helper(List<String> result, StringBuilder sb, int left,
                        int right)
    {
        if (right < left || left < 0)
        {
            return;
        }

        if (right == 0)
        {
            result.add(sb.toString());
        }

        helper(result, sb.append("("), left - 1, right);
        sb.setLength(sb.length() - 1);
        helper(result, sb.append(")"), left, right - 1);
        sb.setLength(sb.length() - 1);
    }
}

