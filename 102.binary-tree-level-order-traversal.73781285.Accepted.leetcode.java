public class Solution
{
    public List<List<Integer>> levelOrder(TreeNode root)
    {
        List result = new ArrayList();
        
        if(root == null)
        {
            return result;
        }

        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);

        while(!queue.isEmpty())
        {
            List level = new ArrayList();
            int size = queue.size();
            
            for(int i = 0; i < size; i++)
            {
                TreeNode node = queue.poll();    
                level.add(node.val);
                
                if(node.left != null)
                {
                    queue.offer(node.left);
                }
                
                if(node.right != null)
                {
                    queue.offer(node.right);
                }
            }
            
            result.add(level);
        }

        return result;
    }
}

