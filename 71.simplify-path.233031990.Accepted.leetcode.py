class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        result = []
        plist = path.split('/')
        for pos in plist:
            if pos:
                if pos == '..':
                    try:

                        result.pop()
                    except:

                        result = []
                elif pos != '.':
                    result.append(pos)
        return '/' + '/'.join(result)
