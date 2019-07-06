public class Solution
{
    public List<List<Integer>> permute(int[] num)
    {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> newNum = new ArrayList<Integer>(num.length);

        for (int data : num)
        {
            newNum.add(data);
        }

        permutation(null, newNum, result);
        return result;
    }
    public void permutation(List<Integer> prefix, List<Integer> suffix,
                            List<List<Integer>> result)
    {
        if (prefix == null)
        {
            prefix = new ArrayList<Integer>();
        }

        if (result == null)
        {
            result = new ArrayList<List<Integer>>();
        }

        if (suffix.size() == 1)
        {
            ArrayList<Integer> newElement = new ArrayList<Integer>(prefix);
            newElement.addAll(suffix);
            result.add(newElement);
        }

        for (int i = 0; i < suffix.size(); i++)
        {
            List<Integer> newPrefix = new ArrayList<Integer>(prefix);
            List<Integer> newSuffix = new ArrayList<Integer>(suffix);
            newPrefix.add(newSuffix.get(i));
            newSuffix.remove(i);
            permutation(newPrefix, newSuffix, result);
        }
    }
}
