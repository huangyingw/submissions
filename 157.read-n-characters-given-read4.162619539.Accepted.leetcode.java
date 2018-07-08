public class Solution extends Reader4
{
    public int read(char[] buf, int n)
    {
        int count = 0;
        char[] buffer = new char[4];

        while (count < n)
        {
            int num = read4(buffer);

            if (num == 0)
            {
                break;
            }

            int index = 0;

            while (index < num && count < n)
            {
                buf[count++] = buffer[index++];
            }
        }

        return count;
    }
}

