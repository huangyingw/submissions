from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        content_to_path = defaultdict(list)
        for path in paths:
            path_list = path.split(" ")
            for f in path_list[1:]:
                open_bracket = f.index("(")
                close_bracket = f.index(")")
                content = f[open_bracket + 1:close_bracket]
                content_to_path[content].append(path_list[0] + "/" + f[:open_bracket])
        return [dup for dup in content_to_path.values() if len(dup) > 1]
