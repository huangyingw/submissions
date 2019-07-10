









class Solution(object):
    def restoreIpAddresses(self, s):

        nb_sections = 4
        if 3 * nb_sections < len(s) < nb_sections:
            return []
        results = [[]]
        while nb_sections > 0:
            new_results = []
            for result in results:
                used = sum((len(section) for section in result))
                remaining = len(s) - used
                if 3 * (nb_sections - 1) >= remaining - 3 >= nb_sections - 1 and 100 <= int(s[used:used + 3]) <= 255:
                    new_results.append(result + [s[used:used + 3]])
                if 3 * (nb_sections - 1) >= remaining - 2 >= nb_sections - 1 and 10 <= int(s[used:used + 2]):
                    new_results.append(result + [s[used:used + 2]])
                if 3 * (nb_sections - 1) >= remaining - 1 >= nb_sections - 1:
                    new_results.append(result + [s[used]])
            nb_sections -= 1
            results = new_results
        return ['.'.join(result) for result in results]
