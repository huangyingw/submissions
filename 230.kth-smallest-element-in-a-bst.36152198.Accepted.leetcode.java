  public class Solution
  {
    private int counter = 0;
    private int result = -1;

    public int kthSmallest(TreeNode root, int k)
    {
      counter = 0;
      inorderTraversal(root, k);
      return result;
    }

    private void inorderTraversal(TreeNode root, int k)
    {
      if (root == null)
      {
        return;
      }

      inorderTraversal(root.left, k);
      counter++ ;

      if (k == counter)
      {
        this.result = root.val;
        return;
      }

      inorderTraversal(root.right, k);
    }
  }

