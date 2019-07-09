_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        results = []

        def num_to_ip(num):
            ip = []
            for _ in range(4):
                num, byte = divmod(num, 256)
                ip.append(str(byte))
            return ".".join(ip[::-1])
        ip_num = 0
        for byte in ip.split("."):
            ip_num = ip_num * 256 + int(byte)
        while n > 0:
            mask = 33 - min((ip_num & -ip_num).bit_length(), n.bit_length())
            results.append(num_to_ip(ip_num) + "/" + str(mask))
            ip_num += 1 << (32 - mask)
            n -= 1 << (32 - mask)
        return results
