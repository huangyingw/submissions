/*
  ✘ Wrong Answer
  ✘ 97/114 cases passed (N/A)
  ✘ testcase: '[1,2]\n1'
  ✘ answer: true
  ✘ expected_answer: false
 */
public class Solution
{
    public boolean hasPathSum(TreeNode root, int sum)
    {
        if (root == null)
        {
            return false;
        }

        if (root.left == null && root.right == null && root.val == sum)
        {
            return true;
        }

        return hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val);
    }
}
