public class Solution
{
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p)
    {
        TreeNode successor = null;

        while (root != null)
        {
            if (root.val > p.val)
            {
                successor = root;
                root = root.left;
            }
            else if (root.val < p.val)
            {
                root = root.right;
            }
            else
            {
                break;
            }
        }

        if (root == null)
        {
            return null;
        }

        if (root.right == null)
        {
            return successor;
        }

        root = root.right;

        while (root.left != null)
        {
            root = root.left;
        }

        return root;
    }
}
