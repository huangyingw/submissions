public class Solution
{
    public String fractionToDecimal(int numerator, int denominator)
    {
        long a = numerator, b = denominator;

        if (b == 0)
        {
            throw new IllegalArgumentException("denominator must be positive");
        }

        StringBuffer result = new StringBuffer();

        if (a * b < 0)
        {
            result.append("-");
        }

        a = Math.abs(a);
        b = Math.abs(b);
        result.append(a / b);

        if (a % b != 0)
        {
            result.append(".");
            Map<Long, Integer> map = new HashMap<Long, Integer>();
            int index = result.length();

            while (a != 0 && map.containsKey(a) == false)
            {
                result.append(a / b);
                map.put(a / b, index++);
                a = a % b * 10;
            }

            if (map.containsKey(a))
            {
                result.insert(map.get(a), "(");
                result.append(")");
            }
        }

        return result.toString();
    }
}

