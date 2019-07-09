_author_ = 'jake'
_project_ = 'leetcode'



















class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            plus = local.index("+")
            if plus != -1:
                local = local[:plus]
            local = local.replace(".", "")
            unique.add(local + domain)
        return len(unique)
