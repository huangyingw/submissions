_author_ = 'jake'
_project_ = 'leetcode'













from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):

        email_to_account = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_account[email].append(i)
        result = []
        visited = [False for _ in range(len(accounts))]

        def dfs(i):
            emails = set()
            if visited[i]:
                return emails
            visited[i] = True
            for email in accounts[i][1:]:
                emails.add(email)
                for account in email_to_account[email]:
                    emails |= dfs(account)
            return emails
        for i, account in enumerate(accounts):
            emails = dfs(i)
            if emails:
                result.append([account[0]] + sorted(list(emails)))
        return result
