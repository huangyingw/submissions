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
        Deque<Integer> dequeue = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++)
        {
            while (!dequeue.isEmpty() && nums[dequeue.getLast()] <= nums[i])
            {
                dequeue.removeLast();
            }

            dequeue.addLast(i);

            while (!dequeue.isEmpty() && dequeue.getLast() - dequeue.getFirst() + 1 > winLen)
            {
                dequeue.removeFirst();
            }

            if (i < winLen - 1)
            {
                continue;
            }

            result[i - (winLen - 1)] = dequeue.getFirst();
        }

        return result;
    }
}
