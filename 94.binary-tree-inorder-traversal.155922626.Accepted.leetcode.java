public class Solution
{
    public ArrayList<Integer> inorderTraversal(TreeNode root)
    {
        ArrayList<Integer> inOrder = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode current = root;

        while (!stack.empty() || current != null)
        {
            if (current != null)
            {
                stack.push(current);
                current = current.left;
            }
            else
            {
                current = stack.pop();
                inOrder.add(current.val);
                current = current.right;
            }
        }

        return inOrder;
    }
}

