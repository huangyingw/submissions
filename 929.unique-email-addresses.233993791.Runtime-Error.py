class Solution:
    def numUniqueEmails(self, emails):
        unique = set()
        for email in emails:
            local, domain = email.split("@")
            plus = local.index("+")
            if plus != -1:
                local = local[:plus]
            local = local.replace(".", "")
            unique.add(local + domain)
        return len(unique)
