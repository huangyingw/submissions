/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution
{
    public int maxDepth(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);
        int depth = 0;

        while (!queue.isEmpty())
        {
            depth++;
            int size = queue.size();

            for (int i = 0; i < size; i++)
            {
                root = queue.poll();

                if (null != root.left)
                {
                    queue.add(root.left);
                }

                if (null != root.right)
                {
                    queue.add(root.right);
                }
            }
        }

        return depth;
    }
}
