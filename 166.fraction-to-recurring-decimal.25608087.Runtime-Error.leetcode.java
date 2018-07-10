class Solution
{
    String fractionToDecimal(int numerator, int denominator)
    {
        StringBuilder out = new StringBuilder();
        Long Numerator = (long) numerator;
        Long Denominator = (long) denominator;

        if (Denominator < 0)
        {
            Denominator = -Denominator;
            Numerator = -Numerator;
        }

        if (Numerator < 0)
        {
            Numerator = -Numerator;
            out.append(" - ");
        }

        out.append((Numerator / Denominator));
        long remainder = Numerator % Denominator;

        if (remainder == 0)
        {
            return out.toString();
        }

        out.append(".");
        List<Long> save = new ArrayList<Long>();
        Map<Long, Long> have = new HashMap<Long, Long>();

        for (Long i = (long) 0; remainder != 0 && (have.get(remainder) == have.size()); ++i)
        {
            have.put(remainder, i);
            remainder *= 10;
            save.add(remainder / Denominator);
            remainder %= Denominator;
        }

        if (remainder != 0)
        {
            for (int j = 0; j < have.get(remainder); ++j)
            {
                out.append(have.get(j));
                out.append("(");
            }

            for (Long j = have.get(remainder); j < save.size(); ++j)
            {
                out.append(have.get(j));
                out.append(")");
            }

            for (int j = 0; j < save.size(); ++j)
            {
                out.append(have.get(j));
            }
        }

        return out.toString();
    }
}
