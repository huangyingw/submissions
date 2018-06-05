public class Solution
{
    public int[] twoSum(final int[] numbers, int target)
    {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] result = new int[2];

        for (int index = 0; index < numbers.length; index++)
        {
            if (map.containsKey(numbers[index]))
            {
                result[0] = map.get(numbers[index]);
                result[1] = index;
                break;
            }
            else
            {
                map.put(target - numbers[index], index);
            }
        }

        return result;
    }
}
