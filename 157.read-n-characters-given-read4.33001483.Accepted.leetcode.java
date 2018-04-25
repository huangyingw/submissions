public class Solution extends Reader4
{
    public int read(char[] buf, int n)
    {
        char[] bb = new char[4];
        int k = read4(bb);
        int cur = 0;
        int index = 0;
        Boolean flag = false;

        while (k > 0)
        {
            if (index >= n)
            {
                break;
            }

            buf[index++ ] = bb[cur++ ];
            k-- ;

            if (k == 0)
            {
                if (flag)
                {
                    break;
                }

                cur = 0;
                k = read4(bb);

                if (k < 4)
                {
                    flag = true;
                }
            }
        }

        return index;
    }
}

