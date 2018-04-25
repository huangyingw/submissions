  public class Solution {
    public void connect(TreeLinkNode root) {
      while (root != null) {
        TreeLinkNode next = null; // the first node of next level
        TreeLinkNode prev = null; // previous node on the same level

        for (; root != null; root = root.next) {
          if (next == null) {
            next = root.left != null ? root.left : root.right;
          }

          if (root.left != null) {
            if (prev != null) {
              prev.next = root.left;
            }
            else {
              prev = root.left;
            }
          }

          if (root.right != null) {
            if (prev != null) {
              prev.next = root.right;
            }
            else {
              prev = root.right;
            }
          }
        }

        root = next; // turn to next level
      }
    }
  }
