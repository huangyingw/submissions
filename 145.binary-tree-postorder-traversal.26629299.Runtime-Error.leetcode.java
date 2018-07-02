public class Solution
{
    public List<Integer> postorderTraversal(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }

        List<Integer> result = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);

        while (!stack.empty() || root != null)
        {
            root = root.left;

            if (root != null)
            {
                stack.push(root);
            }
            else
            {
                root = stack.pop();
                result.add(root.val);
                root = root.right;
            }
        }

        return result;
    }
}
