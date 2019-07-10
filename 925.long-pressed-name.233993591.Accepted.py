_author_ = 'jake'
_project_ = 'leetcode'











class Solution:
    def isLongPressedName(self, name, typed):

        typed_i, name_i = 0, 0
        while name_i < len(name):
            c, c_count = name[name_i], 1
            name_i += 1
            while name_i < len(name) and name[name_i] == c:
                name_i += 1
                c_count += 1
            while typed_i < len(typed) and typed[typed_i] == c:
                typed_i += 1
                c_count -= 1
            if c_count > 0:
                return False
        return typed_i == len(typed)
