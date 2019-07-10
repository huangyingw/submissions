_author_ = 'jake'
_project_ = 'leetcode'



























class Solution(object):
    def isValid(self, code):

        status = "text"
        tag_stack = []
        upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        i = 0
        while i < len(code):
            c = code[i]
            if status == "text":
                if c == "<":
                    if i + 1 < len(code) and code[i + 1] == "/":
                        status = "closing"
                        i += 2
                        tag_start = i
                    elif i + 8 < len(code) and code[i + 1:i + 9] == "![CDATA[" and tag_stack:
                        status = "cdata"
                        i += 9
                    else:
                        status = "opening"
                        i += 1
                        tag_start = i
                elif not tag_stack:
                    return False
                else:
                    i += 1
            elif status in ["opening", "closing"]:
                if code[i] == ">":
                    tag = code[tag_start:i]
                    if len(tag) < 1 or len(tag) > 9:
                        return False
                    if status == "opening":
                        tag_stack.append(tag)
                    else:
                        if not tag_stack or tag_stack.pop() != tag:
                            return False
                        if not tag_stack and i != len(code) - 1:
                            return False
                    status = "text"
                elif c not in upper:
                    return False
                i += 1
            elif status == "cdata":
                if i + 2 < len(code) and code[i:i + 3] == "]]>":
                    i += 3
                    status = "text"
                else:
                    i += 1
        return status == "text" and not tag_stack
