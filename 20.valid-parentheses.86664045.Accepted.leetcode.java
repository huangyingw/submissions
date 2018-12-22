public class Solution
{
    public boolean isValid(String s)
    {
        char[] charArray = s.toCharArray();
        HashMap<Character, Character> map = new HashMap<Character, Character>();
        map.put('(', ')');
        map.put('[', ']');
        map.put('{', '}');
        Stack<Character> stack = new Stack<Character>();

        for (char c : charArray)
        {
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            <<< <<< < Updated upstream
            if (map.containsKey(c))
                == == == =
                    if(map.containsKey(c))
                        >>>>>>> Stashed changes
                {
                    stack.push(c);
                }
                else
                {
                    <<< <<< < Updated upstream

                    if (stack.isEmpty() || map.get(stack.pop()) != c)
                        == == == =
                            if (stack.isEmpty() || map.get(stack.pop()) != c)
                                >>> >>> > Stashed changes
                        {
                            return false;
                        }
                }

            == == == =

                if (map.containsKey(c))
                    == == == =
                        if (map.containsKey(c))
                            >>> >>> > Stashed changes
                {
                    stack.push(c);
                }
                else
                {
                    <<< <<< < Updated upstream

                    if (stack.isEmpty() || map.get(stack.pop()) != c)
                        == == == =
                            if (stack.isEmpty() || map.get(stack.pop()) != c)
                                >>> >>> > Stashed changes
                        {
                            return false;
                        }
                }

            <<< <<< < Updated upstream
            >>> >>> > Stashed changes
            == == == =
                >>> >>> > Stashed changes
                == == == =

                    if (map.containsKey(c))
                        == == == =
                            if (map.containsKey(c))
                                >>> >>> > Stashed changes
                {
                    stack.push(c);
                }
                else
                {
                    <<< <<< < Updated upstream

                    if (stack.isEmpty() || map.get(stack.pop()) != c)
                        == == == =
                            if (stack.isEmpty() || map.get(stack.pop()) != c)
                                >>> >>> > Stashed changes
                        {
                            return false;
                        }
                }

            <<< <<< < Updated upstream
            >>> >>> > Stashed changes
            == == == =
                >>> >>> > Stashed changes
                == == == =

                    if (map.containsKey(c))
                        == == == =
                            if (map.containsKey(c))
                                >>> >>> > Stashed changes
                {
                    stack.push(c);
                }
                else
                {
                    <<< <<< < Updated upstream

                    if (stack.isEmpty() || map.get(stack.pop()) != c)
                        == == == =
                            if (stack.isEmpty() || map.get(stack.pop()) != c)
                                >>> >>> > Stashed changes
                        {
                            return false;
                        }
                }

            <<< <<< < Updated upstream
            >>> >>> > Stashed changes
            == == == =
                >>> >>> > Stashed changes
        }

        return stack.isEmpty();
    }
}
