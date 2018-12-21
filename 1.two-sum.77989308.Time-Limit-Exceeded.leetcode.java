<<< <<< < Updated upstream
public class Solution
{
    public int[] twoSum(final int[] nums, int target)
    == == == =
        public class Solution
    {
        public int[] twoSum(final int[] nums, int target)
        >>> >>> > Stashed changes
        {
            int[] result = new int[2];
            Arrays.sort(nums);
            int left = 0;
            int right = nums.length - 1;
            <<< <<< < Updated upstream

            while (left < right)
            {
                if ((nums[left] + nums[right]) > target)
                {
                    right--;
                }
                else if ((nums[left] + nums[right]) < target)
                    == == == =
                        while (left < right)
                    {
                        if ((nums[left] + nums[right]) > target)
                        {
                            right--;
                        }
                        else if ((nums[left] + nums[right]) < target)
                            >>> >>> > Stashed changes
                        {
                            left++;
                        }
                        else
                        {
                            result[0] = left;
                            result[1] = right;
                        }
                    }

                <<< <<< < Updated upstream
                == == == =
                    >>>>>>> Stashed changes
                    return result;
            }
        }
