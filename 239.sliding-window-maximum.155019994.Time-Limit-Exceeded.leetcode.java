public class Solution
{
    public int[] maxSlidingWindow(int[] nums, int k)
    {
        if (nums == null || nums.length == 0)
        {
            return nums;
        }

        k = Math.min(nums.length, k);
        int[] result = new int[nums.length - k + 1];
        Deque<Integer> deq = new ArrayDeque<>();

        for (int i = 0; i < nums.length; i++)
        {
            System.out.printf("deq --> 1 %s\n",  deq);

            while (!deq.isEmpty() && nums[deq.getLast()] < nums[i])
            {
                System.out.printf("deq.getLast() --> %s\n",  deq.getLast());
                System.out.printf("nums[i] --> %s\n",  nums[i]);
                deq.removeLast();
            }

            System.out.printf("deq --> 2 %s\n",  deq);
            deq.addLast(i);
            System.out.printf("deq --> 3 %s\n",  deq);

            while (deq.getLast() - deq.getFirst() + 1 > k)
            {
                deq.removeFirst();
            }

            System.out.printf("deq --> 4 %s\n",  deq);

            if (i >= k - 1)
            {
                result[i - (k - 1)] = nums[deq.getFirst()];
                System.out.printf("result[%s] --> %s\n", i - (k - 1), result[i - (k - 1)]);
            }
        }

        return result;
    }
}

