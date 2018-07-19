public class Solution
{
    private void preorderTraversal(TreeNode root, ArrayList<Integer> preorder)
    {
        if (root == null)
        {
            return;
        }

        preorder.add(root.val);
        preorderTraversal(root.left, preorder);
        preorderTraversal(root.right, preorder);
    }

    public ArrayList<Integer> preorderTraversal(TreeNode root)
    {
        ArrayList<Integer> preorder = new ArrayList<Integer>();
        preorderTraversal(root, preorder);
        return preorder;
    }
}
