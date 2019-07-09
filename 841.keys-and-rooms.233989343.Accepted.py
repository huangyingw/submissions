_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)
        dfs(0)
        return len(visited) == len(rooms)
