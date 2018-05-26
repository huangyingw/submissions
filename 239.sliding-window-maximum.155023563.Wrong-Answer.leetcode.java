public class Solution
{
    public int[] maxSlidingWindow(int[] nums, int k)
    {
        k = Math.min(nums.length, k);
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> deq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++)
        {
            while (!deq.isEmpty() && nums[deq.getLast()] <= nums[i])
            {
                deq.removeLast();
            }

            deq.addLast(i);

            while (!deq.isEmpty() && i - deq.getFirst() + 1 > k)
            {
                deq.removeFirst();
            }

            if (i >= k - 1)
            {
                result[i - (k - 1)] = nums[deq.getFirst()];
            }
        }

        return result;
    }
}
