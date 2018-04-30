  public class Solution
  {
    public int kthSmallest(TreeNode root, int k)
    {
      Stack<TreeNode> stack = new Stack<TreeNode>();
      TreeNode node = root;
      int res = 0;

      while (node != null || !stack.isEmpty())
      {
        if (node != null)
        {
          stack.push(node);
          node = node.left;
        }
        else
        {
          node = stack.pop();

          if (--k == 0)
          {
            return node.val;
          }

          node = node.right;
        }
      }

      return res;
    }
  }

