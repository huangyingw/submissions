public class Solution
{
    public List<List<String>> partition(String s)
    {
        List<List<String>> result = new ArrayList<List<String>>();

        ArrayList<String> current = new ArrayList<String>();
        dfs(s, 0, current, result);
        return result;
    }

    private void dfs(String str, int start, ArrayList<String> current, List<List<String>> result)
    {
        if (start == str.length())
        {
            result.add(new ArrayList<String>(current));
            return;
        }

        for (int i = start + 1; i <= str.length(); i++)
        {
            String subStr = str.substring(start, i);

            if (isPalindrome(subStr))
            {
                current.add(subStr);
                dfs(str, i, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String str)
    {
        int left = 0;
        int right = str.length() - 1;

        while (left < right)
        {
            if (str.charAt(left) != str.charAt(right))
            {
                return false;
            }

            left++ ;
            right-- ;
        }

        return true;
    }
}
