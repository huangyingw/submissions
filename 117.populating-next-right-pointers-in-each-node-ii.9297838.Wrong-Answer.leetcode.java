  public class Solution {
    public void connect(TreeLinkNode root) {
      TreeLinkNode next = null; // the first node of next level

      while (root != null) {
        TreeLinkNode prev = null; // previous node on the same level

        for (; root != null; root = root.next) {
          next = root.left != null ? root.left : root.right;

          if (root.left != null) {
            if (prev != null) {
              prev.next = root.left;
            }

            prev = root.left;
          }

          if (root.right != null) {
            if (prev != null) {
              prev.next = root.right;
            }

            prev = root.right;
          }
        }

        root = next; // turn to next level
      }
    }
  }

