public class Solution
{
    public int[] twoSum(int[] nums, int target)
    {
        int left = 0, right = nums.length - 1;
        int[] result = new int[2];
        Arrays.sort(nums);

        while (left < right)
        {
            if (nums[left] + nums[right] == target)
            {
                result[0] = left;
                result[1] = right;
                break;
            }
            else if (nums[left] + nums[right] > target)
            {
                right--;
            }
            else
            {
                left++;
            }
        }

        return result;
    }
}
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
<<< <<< < Updated upstream
== == == =

    >>>>>>> Stashed changes
    == == == =

        >>>>>>> Stashed changes
        == == == =

            >>>>>>> Stashed changes
            == == == =

                >>>>>>> Stashed changes
                == == == =

                    >>>>>>> Stashed changes
                    == == == =

                        >>>>>>> Stashed changes
                        == == == =

                            >>>>>>> Stashed changes
                            == == == =

                                >>>>>>> Stashed changes
