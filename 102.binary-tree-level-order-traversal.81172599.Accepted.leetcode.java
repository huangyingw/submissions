public class Solution
{
    private void traversal(TreeNode root, int level, List<List<Integer>> result)
    {
        if (root == null)
        {
            return;
        }

        if (level >= result.size())
        {
            result.add(new ArrayList<Integer>());
        }

        result.get(level).add(root.val);
        traversal(root.left, level + 1, result);
        traversal(root.right, level + 1, result);
    }
    
    public List<List<Integer>> levelOrder(TreeNode root)
    {
      List<List<Integer>> result = new ArrayList<List<Integer>>();
      traversal(root, 0, result);
      return result;
    }
}
