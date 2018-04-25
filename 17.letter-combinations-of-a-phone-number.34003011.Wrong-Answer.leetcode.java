public class Solution
{
    public ArrayList<String> letterCombinations(String digits)
    {
        String[] dic =
        { " ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        ArrayList<String> res = new ArrayList<String>();
        res.add("");

        if (digits == null || digits.length() == 0)
        {
            return res;
        }

        for (int i = 0; i < digits.length(); i++)
        {
            String letters = dic[digits.charAt(i) - '0'];
            ArrayList<String> newRes = new ArrayList<String>();

            for (int j = 0; j < res.size(); j++)
            {
                for (int k = 0; k < letters.length(); k++)
                {
                    newRes.add(res.get(j) + Character.toString(letters.charAt(k)));
                }
            }

            res = newRes;
        }

        return res;
    }
}

