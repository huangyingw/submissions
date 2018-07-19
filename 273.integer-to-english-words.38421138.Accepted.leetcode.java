public class Solution
{
    public String numberToWords(int num)
    {
        String res = convertHundred(num % 1000);
        String[] v = { "Thousand", "Million", "Billion" };

        for (int i = 0; i < 3; ++i)
        {
            num /= 1000;
            res = num % 1000 > 0
                  ? convertHundred(num % 1000) + " " + v[i] + " " + res : res;
        }

        res = res.trim();
        return res.isEmpty() ? "Zero" : res;
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
        String res;
        int a = num / 100, b = num % 100, c = num % 10;
        res = b < 20 ? v1[b] : v2[b / 10] + (c > 0 ? " " + v1[c] : "");

        if (a > 0)
        {
            res = v1[a] + " Hundred" + (b > 0 ? " " + res : "");
        }

        return res;
    }
}
