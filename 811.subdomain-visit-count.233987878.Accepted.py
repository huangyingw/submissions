_author_ = 'jake'
_project_ = 'leetcode'













from collections import defaultdict


class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counts = defaultdict(int)
        for cpdomain in cpdomains:
            count, domains = cpdomain.split(" ")
            domains = domains.split(".")
            for i in range(len(domains)):
                domain = ".".join(domains[i:])
                counts[domain] += int(count)
        return [str(count) + " " + domain for domain, count in counts.items()]
