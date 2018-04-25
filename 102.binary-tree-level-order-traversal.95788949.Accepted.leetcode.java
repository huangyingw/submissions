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
            List<Integer> local = new ArrayList<Integer>();
            
            for (int i = 0; i < size; i++)
            {
                root = queue.poll();
                local.add(root.val);
                
                if (null != root.left)
                {
                    queue.add(root.left);
                }
                
                if (null != root.right)
                {
                    queue.add(root.right);
                }
            }

            result.add(local);
        }
        
        return result;
    }
}
