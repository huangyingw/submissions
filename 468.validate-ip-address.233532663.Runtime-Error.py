_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        ip_list = IP.split(".")
        if len(ip_list) == 4:
            for group in ip_list:
                n = int(group)
                if n < 0 or n > 255 or len(str(n)) != len(group):
                    return "Neither"
            return "IPv4"
        ip_list = IP.split(":")
        if len(ip_list) != 8:
            return "Neither"
        for group in ip_list:
            n = int(group, 16)
            if n < 0 or n > int("FFFF", 16) or len(group) > 4 or group[0] == "-":
                return "Neither"
        return "IPv6"
