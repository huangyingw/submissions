public class Solution
{
    public ArrayList<ArrayList<Integer>> permute(int[] num)
    {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> element = new ArrayList<Integer>();
        boolean[] visited = new boolean[num.length];
        helper(num, result, element, visited);
        return result;
    }

    public void helper(int[] num, ArrayList<ArrayList<Integer>> result,
                       ArrayList<Integer> element, boolean[] visited)
    {
        if (element.size() == num.length)
        {
            // duplicate element and add it to result (element would be changed from
            // time to time. If directly use element
            // only result would be changed when element changed)
            result.add(new ArrayList<Integer>(element));
            return;
        }

        for (int i = 0; i < num.length; i++)
        {
            if (!visited[i])
            {
                visited[i] = true;
                element.add(num[i]);
                helper(num, result, element, visited);
                // After providing a complete permutation, pull out the last number,
                element.remove(element.size() - 1);
                visited[i] = false;
            }
        }
    }
}
