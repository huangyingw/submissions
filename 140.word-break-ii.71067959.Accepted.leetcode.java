public class Solution
{
    private ArrayList<String> dfs(String s, Set<String> dict,
                                  Map<String, ArrayList<String>> solutions)
    {
        ArrayList<String> solution = solutions.get(s);

        if (solution != null)
        {
            return solution;
        }

        solution = new ArrayList<String>();

        for (int i = 1; i < s.length(); i++)
        {
            String prefix = s.substring(0, i);

            if (dict.contains(prefix))
            {
                for (String subfix : dfs(s.substring(i), dict, solutions))
                {
                    solution.add(prefix + " " + subfix);
                }
            }
        }

        if (dict.contains(s))
        {
            solution.add(s);
        }

        solutions.put(s, solution);
        return solution;
    }

    public List<String> wordBreak(String s, Set<String> dict)
    {
        return dfs(s, dict, new HashMap<String, ArrayList<String>>());
    }
}

