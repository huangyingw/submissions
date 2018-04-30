public class Solution
{
    public int[] maxSlidingWindow(int[] nums, int winLen)
    {
        if (nums == null || nums.length == 0)
        {
            return nums;
        }

        winLen = Math.min(nums.length, winLen);
        int[] result = new int[nums.length - winLen + 1];
        Deque<Integer> deq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++)
        {
            while (!deq.isEmpty() && nums[deq.getLast()] <= nums[i])
            {
                deq.removeLast();
            }

            deq.addLast(nums[i]);

            if (i < winLen - 1)
            {
                continue;
            }

            while (!deq.isEmpty() && deq.getLast() - deq.getFirst() + 1 > winLen)
            {
                deq.removeFirst();
            }

            result[i - (winLen - 1)] = deq.getFirst();
        }

        return result;
    }
}
