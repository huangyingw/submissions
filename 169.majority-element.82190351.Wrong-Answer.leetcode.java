<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
public class Solution
{
    public int majorityElement(int[] nums)
    == == == =
        public class Solution
    {
        public int majorityElement(int[] nums)
        >>> >>> > Stashed changes
        {
            int result = nums[0];
            int count = 1;

            <<< <<< < Updated upstream

            for (int nav = 1; nav < nums.length; nav++)
            {
                if (nums[nav] == result)
                    == == == =
                    for (int nav = 1; nav < nums.length; nav++)
                    {
                        if (nums[nav] == result)
                            >>> >>> > Stashed changes
                        {
                            count ++;
                        }
                        else
                        {
                            count --;
                            <<< <<< < Updated upstream
                            if (count == 0)
                                == == == =
                                    if(count == 0)
                                        >>>>>>> Stashed changes
                                {
                                    result = nums[nav];
                                }
                        }
                    }

                return result;
            }
        }
        == == == =
            public class Solution
        {
            public int majorityElement(int[] nums)
            {
                int result = nums[0];
                int count = 1;

                for (int nav = 1; nav < nums.length; nav++)
                {
                    if (nums[nav] == result)
                    {
                        count ++;
                    }
                    else
                    {
                        count --;

                        if (count == 0)
                        {
                            result = nums[nav];
                        }
                    }
                }

                return result;
            }
        }
        >>> >>> > Stashed changes
        == == == =
            public class Solution
        {
            public int majorityElement(int[] nums)
            {
                int result = nums[0];
                int count = 1;

                for (int nav = 1; nav < nums.length; nav++)
                {
                    if (nums[nav] == result)
                    {
                        count ++;
                    }
                    else
                    {
                        count --;

                        if (count == 0)
                        {
                            result = nums[nav];
                        }
                    }
                }

                return result;
            }
        }
        >>> >>> > Stashed changes
