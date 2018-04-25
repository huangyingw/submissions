public class Solution
{
    public boolean verifyPreorder(int[] preorder)
    {
        int low = Integer.MIN_VALUE, index = -1;

        for (int i : preorder)
        {
            if (i < low)
            {
                return false;
            }

            while (index >= 0 && i > preorder[index])
            {
                low = preorder[index--];
            }

            preorder[++index] = i;
        }

        return true;
    }
}
