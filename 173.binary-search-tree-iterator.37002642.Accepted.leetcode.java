public class BSTIterator
    {
      private Stack<TreeNode> stack = new Stack<>();
      private TreeNode curt;

      public BSTIterator(TreeNode root)
      {
        curt = root;
      }

      public boolean hasNext()
      {
        return (curt != null || !stack.isEmpty());
      }

      public int next()
      {
        while (curt != null)
        {
          stack.push(curt);
          curt = curt.left;
        }

        curt = stack.pop();
        int result = curt.val;
        curt = curt.right;
        return result;
      }
    }
