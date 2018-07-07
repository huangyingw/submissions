public class Solution extends Reader4
{
    public int read(char[] buf, int n)
    {
        System.out.printf("n --> %s\n", n);
        char[] buffer = new char[4];
        int readBytes = 0;
        boolean eof = false;

        while (!eof && readBytes < n)
        {
            int sz = read4(buffer);

            if (sz == 0)
            {
                eof = true;
            }

            System.out.printf("sz --> %s\n", sz);
            int bytes = Math.min(n - readBytes, sz);
            System.out.printf("bytes --> %s\n", bytes);
            System.arraycopy(buffer, 0, buf, readBytes, bytes);
            readBytes += bytes;
            System.out.printf("readBytes --> %s\n", readBytes);
        }

        return readBytes;
    }
}

