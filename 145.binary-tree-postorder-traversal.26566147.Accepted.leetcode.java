public class Solution
{
    public ArrayList<Integer> postorderTraversal(TreeNode root)
    {
        ArrayList<Integer> postorder = new ArrayList<Integer>();

        if (root == null)
        {
            return postorder;
        }

        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode prev = null;
        stack.push(root);

        while (!stack.isEmpty())
        {
            TreeNode current = stack.peek();

            if (prev == null || prev.left == current || prev.right == current)
            {
                if (current.left != null)
                {
                    stack.push(current.left);
                }
                else if (current.right != null)
                {
                    stack.push(current.right);
                }
            }
            else if (current.left == prev)
            {
                if (current.right != null)
                {
                    stack.push(current.right);
                }
            }
            else
            {
                postorder.add(current.val);
                stack.pop();
            }

            prev = current;
        }

        return postorder;
    }
}
