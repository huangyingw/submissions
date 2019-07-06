public class BSTIterator
{
    Stack<TreeNode> stack;
    public BSTIterator(TreeNode root)
    {
        stack = new Stack<TreeNode>();
        pushLeft(root);
    }
    public void pushLeft(TreeNode node)
    {
        while (node != null)
        {
            stack.push(node);
            node = node.left;
        }
    }
    public boolean hasNext()
    {
        return !stack.isEmpty();
    }
    public int next()
    {
        TreeNode node = stack.pop();
        int result = node.val;

        if (node.right != null)
        {
            node = node.right;
            pushLeft(node);
        }

        return result;
    }
}
