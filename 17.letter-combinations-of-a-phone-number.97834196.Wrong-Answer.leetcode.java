public class Solution
{
    public ArrayList<String> letterCombinations(String digits)
    {
        String[] dic = { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        ArrayList<String> result = new ArrayList<String>();
        StringBuilder current = new StringBuilder();
        dfs(digits, dic, 0, current, result);
        return result;
    }
    public void dfs(String digits, String[] dic, int deep, StringBuilder current, ArrayList<String> result)
    {
        if (deep == digits.length())
        {
            result.add(current.toString());
            return;
        }
        else
        {
            String dicStr = dic[digits.charAt(deep) - '0'];

            for (int i = 0; i < dicStr.length(); i++)
            {
                current.append(dicStr.charAt(i));
                dfs(digits, dic, deep + 1, current, result);
                current.deleteCharAt(current.length() - 1);
            }
        }
    }
}
