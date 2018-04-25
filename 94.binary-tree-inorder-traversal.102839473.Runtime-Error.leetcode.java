public class Solution
{
    public ArrayList<Integer> inorderTraversal(TreeNode root)
    {
        ArrayList<Integer> inOrder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);

        while (!stack.empty())
        {
            if (root != null)
            {
                stack.push(root);
                root = root.left;
            }
            else
            {
                root = stack.pop();
                inOrder.add(root.val);
                root = root.right;
            }
        }

        return inOrder;
    }
}
