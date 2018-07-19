public class Solution
{
    public void connect(TreeLinkNode root)
    {
        if (root == null)
        {
            return;
        }

        if (root.left != null)
        {
            root.left.next = root.right;
        }

        connect(root.left);
        connect(root.right);
    }
}
