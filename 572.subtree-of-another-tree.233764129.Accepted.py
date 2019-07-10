









class Solution(object):
    def isSubtree(self, s, t):

        def serialize(node):
            if not node:
                serial.append("
                return
            serial.append(",")
            serial.append(str(node.val))
            serialize(node.left)
            serialize(node.right)
        serial = []
        serialize(s)
        s_serial = "".join(serial)
        serial = []
        serialize(t)
        t_serial = "".join(serial)
        return t_serial in s_serial
