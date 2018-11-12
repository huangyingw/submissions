public class Solution
{
    public int minMeetingRooms(Interval[] intervals)
    {
        if (intervals == null || intervals.length == 0)
        {
            return 0;
        }

        Arrays.sort(intervals, new Comparator<Interval>()
        {
            public int compare(Interval i1, Interval i2)
            {
                return i1.start - i2.start;
            }
        });
        PriorityQueue<Integer> endTimes = new PriorityQueue<Integer>();
        endTimes.offer(intervals[0].end);

        for (int i = 1; i < intervals.length; i++)
        {
            if (intervals[i].start >= endTimes.peek())
            {
                endTimes.poll();
            }

            endTimes.offer(intervals[i].end);
        }

        return endTimes.size();
    }
}
