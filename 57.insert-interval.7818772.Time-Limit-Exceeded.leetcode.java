public class Solution
{
    public ArrayList<Interval> insert(ArrayList<Interval> intervals,
                                      Interval newInterval)
    {
        for (int i = 0; i < intervals.size(); i++)
        {
            Interval interval = intervals.get(i);

            if (newInterval.end < interval.start)
            {
                intervals.add(i, newInterval);
                return intervals;
            }
            else if (newInterval.start >= interval.end)
            {
                continue;
            }
            else
            {
                newInterval.start = Math.min(newInterval.start,
                                             interval.start);
                newInterval.end = Math.max(newInterval.end, interval.end);
                intervals.add(i, newInterval);
            }
        }

        intervals.add(newInterval);
        return intervals;
    }
}
