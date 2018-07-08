public class Solution extends Reader4
{
    public int read(char[] buf, int n)
    {
        char[] buffer = new char[4];
        int haveRead = 0;
        boolean eof = false;

        while (!eof)
        {
            int oneRead = read4(buffer);

            if (oneRead < 4)
            {
                eof = true;
            }

            int actRead = Math.min(n - haveRead, oneRead);

            for (int i = 0; i < actRead; i++)
            {
                buf[haveRead + i] = buffer[i];
            }

            haveRead += actRead;
        }

        return haveRead;
    }
}

