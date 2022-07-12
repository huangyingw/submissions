class Solution(object):
    def simplifyPath(self, path):

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
