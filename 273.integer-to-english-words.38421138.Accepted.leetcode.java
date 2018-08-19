public class Solution
{
    public String numberToWords(int num)
    {
        String result = convertHundred(num % 1000);
        String[] v = { "Thousand", "Million", "Billion" };

        for (int i = 0; i < 3; ++i)
        {
            num /= 1000;
            result = num % 1000 > 0 ? convertHundred(num % 1000) + " " + v[i] + " " + result : result;
        }

        result = result.trim();
        return result.isEmpty() ? "Zero" : result;
    }

    String convertHundred(int num)
    {
        String[] v1 = { "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                        "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
                        "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
                      };
        String[] v2 = { "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                        "Seventy", "Eighty", "Ninety"
                      };
        String result;
        int a = num / 100, b = num % 100, c = num % 10;
        result = b < 20 ? v1[b] : v2[b / 10] + (c > 0 ? " " + v1[c] : "");

        if (a > 0)
        {
            result = v1[a] + " Hundred" + (b > 0 ? " " + result : "");
        }

        return result;
    }
}
