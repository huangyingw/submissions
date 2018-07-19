public class Solution
{
    public ArrayList<Integer> findSubstring(String S, String[] L)
    {
        ArrayList<Integer> result = new ArrayList<Integer>();
        HashMap<String, Integer> toFind = new HashMap<String, Integer>();
        HashMap<String, Integer> found = new HashMap<String, Integer>();

        for (int i = 0; i < L.length; i ++)
        {
            if (!toFind.containsKey(L[i]))
            {
                toFind.put(L[i], 1);
            }
            else
            {
                toFind.put(L[i], toFind.get(L[i]) + 1);
            }
        }

        for (int i = 0; i <= S.length() - L[0].length() * L.length; i ++)
        {
            found.clear();
            int j;

            for (j = 0; j < L.length; j ++)
            {
                int k = i + j * L[0].length();
                String stub = S.substring(k, k + L[0].length());

                if (!toFind.containsKey(stub))
                {
                    break;
                }

                if (!found.containsKey(stub))
                {
                    found.put(stub, 1);
                }
                else
                {
                    found.put(stub, found.get(stub) + 1);
                }

                if (found.get(stub) > toFind.get(stub))
                {
                    break;
                }
            }

            if (j == L.length)
            {
                result.add(i);
            }
        }

        return result;
    }
}
