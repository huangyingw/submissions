public class Solution
{
    public List<List<Integer>> levelOrder(TreeNode root)
    {
        List result = new ArrayList();

        if (root == null)
        {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.add(root);

        while (!queue.isEmpty())
        {
            int size = queue.size();
            List<Integer> level = new ArrayList<Integer>();

            for (int i = 0; i < size; i++)
            {
                TreeNode node = queue.poll();
                level.add(node.val);

                if (node.left != null)
                {
                    queue.offer(node.left);
                }

                if (node.right != null)
                {
                    queue.offer(node.right);
                }
            }

            result.add(level);
        }

        return result;
    }
}