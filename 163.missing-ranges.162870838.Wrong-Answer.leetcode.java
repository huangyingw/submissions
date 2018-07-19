public class Solution
{
    List<String> findMissingRanges(int[] A, int lower, int upper)
    {
        List<String> ranges = new ArrayList<String>();

        for (int i = 0; lower <= upper && i < A.length; i++)
        {
            if (A[i] > lower)
            {
                ranges.add(getRange(lower, A[i] - 1));
                lower = A[i] + 1;
            }
            else if (A[i] == lower)
            {
                lower++;
            }
        }

        if (lower <= upper)
        {
            ranges.add(getRange(lower, upper));
        }

        return ranges;
    }

    private String getRange(int from, int to)
    {
        return (from == to) ? String.valueOf(from) : from + "->" + to;
    }
}

