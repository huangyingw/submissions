  public class Solution
  {
    public ArrayList<Integer> postorderTraversal(TreeNode root)
    {
      ArrayList<Integer> postOrder = new ArrayList<Integer>();

      if (root == null)
      {
        return postOrder;
      }

      Stack<TreeNode> stack = new Stack<TreeNode>();
      stack.push(root);

      while (stack.size() != 0)
      {
        TreeNode top = stack.peek();

        if (top.left == null && top.right == null)
        {
          postOrder.add(top.val);
          stack.pop();
        }
        else if (top.left != null)
        {
          stack.push(top.left);
          top.left = null;
        }
        else if (top.right != null)
        {
          stack.push(top.right);
          top.right = null;
        }
      }

      return postOrder;
    }
  }

