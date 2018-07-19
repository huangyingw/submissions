public class Solution
{
    public ArrayList<Integer> postorderTraversal(TreeNode root)
    {
        ArrayList<Integer> postOrder = new ArrayList<Integer>();
        postorderTraversal(root, postOrder);
        return postOrder;
    }

    private void postorderTraversal(TreeNode root, ArrayList<Integer> postOrder)
    {
        if (root == null)
        {
            return;
        }

        postOrder.add(root.val);
        postorderTraversal(root.left, postOrder);
        postorderTraversal(root.right, postOrder);
    }
}
