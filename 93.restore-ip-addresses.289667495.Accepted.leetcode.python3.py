class Solution(object):
    def restoreIpAddresses(self, s):
        NB_SECTIONS = 4
        if 3 * NB_SECTIONS < len(s) < NB_SECTIONS:
            return []
        results = [[]]
        while NB_SECTIONS > 0:
            new_results = []
            for result in results:
                used = sum((len(section) for section in result))
                remaining = len(s) - used
                if 3 * (NB_SECTIONS - 1) >= remaining - 3 >= NB_SECTIONS - 1 and 100 <= int(s[used:used + 3]) <= 255:
                    new_results.append(result + [s[used:used + 3]])
                if 3 * (NB_SECTIONS - 1) >= remaining - 2 >= NB_SECTIONS - 1 and 10 <= int(s[used:used + 2]):
                    new_results.append(result + [s[used:used + 2]])
                if 3 * (NB_SECTIONS - 1) >= remaining - 1 >= NB_SECTIONS - 1:
                    new_results.append(result + [s[used]])
            NB_SECTIONS -= 1
            results = new_results
        return ['.'.join(result) for result in results]
