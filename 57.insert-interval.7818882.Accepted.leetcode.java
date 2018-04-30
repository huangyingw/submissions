public class Solution
{

    public ArrayList<Interval> insert(ArrayList<Interval> intervals,
                                      Interval newInterval)
    {
        ArrayList<Interval> result = new ArrayList<Interval>();

        if (newInterval == null)
        {
            return intervals;
        }

        if (intervals == null || intervals.size() == 0)
        {
            result.add(newInterval);
            return result;
        }

        for (Interval temp : intervals)
        {
            if (temp.end < newInterval.start)
            {
                result.add(temp);
            }
            else if (temp.start > newInterval.end)
            {
                result.add(newInterval);
                newInterval = temp;
            }
            else
            {
                newInterval.start = Math.min(newInterval.start, temp.start);
                newInterval.end = Math.max(newInterval.end, temp.end);
            }
        }

        result.add(newInterval);
        return result;
    }
}

