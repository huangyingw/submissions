public class Solution
{
    public List<Integer> inorderTraversal(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }

        List<Integer> result = new ArrayList<Integer>();
        inorderTraversal(root, result);
        return result;
    }

    public void inorderTraversal(TreeNode root, List<Integer> result)
    {
        if (root == null)
        {
            return;
        }

        inorderTraversal(root.left, result);
        result.add(root.val);
        inorderTraversal(root.right, result);
    }
}

