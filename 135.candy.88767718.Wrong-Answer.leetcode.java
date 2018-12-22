public class Solution
{
    public int candy(int[] ratings)
    {
        int n = ratings.length;
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        == == == =
            >>>>>>> Stashed changes

            if (n == 1)
        {
            return 1;
        }

        <<< <<< < Updated upstream
        == == == =
            >>>>>>> Stashed changes
            int[] candies = new int[n];
        == == == =

            if (n == 1)
        {
            return 1;
        }

        int[] candies = new int[n];
        >>> >>> > Stashed changes
        == == == =

            if (n == 1)
        {
            return 1;
        }

        int[] candies = new int[n];
        >>> >>> > Stashed changes
        == == == =

            if (n == 1)
        {
            return 1;
        }

        int[] candies = new int[n];
        >>> >>> > Stashed changes
        == == == =

            if (n == 1)
        {
            return 1;
        }

        int[] candies = new int[n];
        >>> >>> > Stashed changes
        == == == =

            if (n == 1)
        {
            return 1;
        }

        int[] candies = new int[n];
        >>> >>> > Stashed changes
        == == == =

            if (n == 1)
        {
            return 1;
        }

        int[] candies = new int[n];
        >>> >>> > Stashed changes
        Arrays.fill(candies, 1);

        for (int i = 1; i < n; i++)
        {
            if (ratings[i] > ratings[i - 1])
            {
                candies[i] = candies[i - 1] + 1;
            }
        }

        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        <<< <<< < Updated upstream
        int count = candies[n - 1];
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes
        == == == =
            int count = candies[n - 1];
        >>> >>> > Stashed changes

        for (int i = n - 2; i > 0; i--)
        {
            if (ratings[i] > ratings[i + 1] && candies[i] <= candies[i + 1])
            {
                candies[i] = candies[i + 1] + 1;
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
                >>> >>> > Stashed changes
                count += candies[i];
        }

        == == == =
            count += candies[i];
    }

    >>> >>> > Stashed changes
    count += candies[0];
    return count;
}
== == == =

    count += candies[i];
}

count += candies[0];
return count;
}
>>> >>> > Stashed changes
== == == =

    count += candies[i];
}

count += candies[0];
return count;
}
>>> >>> > Stashed changes
== == == =

    count += candies[i];
}

count += candies[0];
return count;
}
>>> >>> > Stashed changes
== == == =

    count += candies[i];
}

count += candies[0];
return count;
}
>>> >>> > Stashed changes
== == == =

    count += candies[i];
}

count += candies[0];
return count;
}
>>> >>> > Stashed changes
== == == =

    count += candies[i];
}

count += candies[0];
return count;
}
>>> >>> > Stashed changes
}
