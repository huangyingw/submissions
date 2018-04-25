public class Solution
{
    public int minDepth(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        LinkedList queue = new LinkedList();
        int curNum = 0;
        int lastNum = 1;
        int level = 1;
        queue.offer(root);

        while (!queue.isEmpty())
        {
            TreeNode cur = (TreeNode) queue.poll();

            if (cur.left == null && cur.right == null)
            {
                return level;
            }

            lastNum-- ;

            if (cur.left != null)
            {
                queue.offer(cur.left);
                curNum++ ;
            }

            if (cur.right != null)
            {
                queue.offer(cur.right);
                curNum++ ;
            }

            if (lastNum == 0)
            {
                lastNum = curNum;
                curNum = 0;
                level++ ;
            }
        }

        return 0;
    }
}

