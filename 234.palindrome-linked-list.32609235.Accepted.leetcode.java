  public class Solution
  {
    public boolean isPalindrome(ListNode head)
    {
      if (head == null)
      {
        return true;
      }

      ListNode slow = head;
      ListNode fast = slow.next;

      while (fast != null && fast.next != null && fast.next.next != null)
      {
        slow = slow.next;
        fast = fast.next.next;
      }

      ListNode p = slow.next;
      ListNode q;
      ListNode end = null;

      while (p != null)
      {
        q = p.next;
        p.next = end;
        end = p;
        p = q;
      }

      while (head != null && end != null)
      {
        if (head.val != end.val)
        {
          return false;
        }

        head = head.next;
        end = end.next;
      }

      return true;
    }
  }

