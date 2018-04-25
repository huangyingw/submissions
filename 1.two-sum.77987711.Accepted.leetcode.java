public class Solution
{
    public int[] twoSum(final int[] numbers, int target)
    {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int[] result = new int[2];

        for (int i = 0; i < numbers.length; i++)
        {
            if (map.containsKey(target - numbers[i]))
            {
                int index = map.get(target - numbers[i]);
                result[0] = index;
                result[1] = i;
                break;
            }
            else
            {
                map.put(numbers[i], i);
            }
        }

        return result;
    }
}

