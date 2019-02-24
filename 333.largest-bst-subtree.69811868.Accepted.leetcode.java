public class Solution
{
    private int result = 0;
    public int largestBSTSubtree(TreeNode root)
    {
        largestBSTHelper(root);
        return result;
    }
    private Data largestBSTHelper(TreeNode root)
    {
        Data current = new Data();

        if (root == null)
        {
            current.isBST = true;
            current.size = 0;
            return current;
        }

        Data left = largestBSTHelper(root.left);
        Data right = largestBSTHelper(root.right);
        current.min = Math.min(root.val, Math.min(right.min, left.min));
        current.max = Math.max(root.val, Math.max(right.max, left.max));

        if (left.isBST && root.val > left.max && right.isBST
                && root.val < right.min)
        {
            current.isBST = true;
            current.size = 1 + left.size + right.size;

            if (current.size > result)
            {
                result = current.size;
            }
        }
        else
        {
            current.size = 0;
        }

        return current;
    }
}
class Data
{
    boolean isBST = false;
    // the minimum for right sub tree or the maximum for right sub tree
    int min = Integer.MAX_VALUE;
    int max = Integer.MIN_VALUE;
    // if the tree is BST, size is the size of the tree; otherwise zero
    int size;
}
