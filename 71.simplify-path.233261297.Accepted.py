_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        result = []
        for item in path_list:
            if item == '..':
                if result:
                    result.pop()
            elif item and item != '.':
                result.append(item)

        return '/' + '/'.join(result)
