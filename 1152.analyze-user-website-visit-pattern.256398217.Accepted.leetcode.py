from collections import defaultdict
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        user_sites = defaultdict(list)
        for _, user, site in sorted(zip(timestamp, username, website)):
            user_sites[user].append(site)
        pattern_to_count = defaultdict(set)
        for user, sites in user_sites.items():
            n = len(sites)
            for i in range(n - 2):
                for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):
                        pattern_to_count[(sites[i], sites[j], sites[k])].add(user)
        max_count = len(max(pattern_to_count.values(), key=len))
        return min(key for key, value in pattern_to_count.items() if len(value) == max_count)
