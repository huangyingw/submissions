  public class Solution
  {
    public ArrayList<Integer> preorderTraversal(TreeNode root)
    {
      ArrayList<Integer> preOrder = new ArrayList<Integer>();
      Stack<TreeNode> stack = new Stack<TreeNode>();

      if (root != null)
      {
        stack.push(root);

        while (!stack.isEmpty())
        {
          root = stack.pop();

          while (root != null)
          {
            preOrder.add(root.val);

            if (root.right != null)
            {
              stack.push(root.right);
            }

            root = root.left;
          }
        }
      }

      return preOrder;
    }
  }

