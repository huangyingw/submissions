public class Solution
{
    public List<String> letterCombinations(String digits)
    {
        String[] letters =
        { "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
        List<String> result = new LinkedList<>();

        if (digits == null || digits.length() == 0)
        {
            return result;
        }

        LinkedList<String> list = new LinkedList<>();
        list.add("");

        for (int i = 0; i < digits.length(); i++)
        {
            int num = digits.charAt(i) - '2';
            int size = list.size();

            for (int k = 0; k < size; k++)
            {
                String tmp = list.pop();

                for (int j = 0; j < letters[num].length(); j++)
                {
                    list.add(tmp + letters[num].charAt(j));
                }
            }
        }

        result.addAll(list);
        return result;
    }
}

