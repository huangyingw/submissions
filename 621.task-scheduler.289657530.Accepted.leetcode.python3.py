class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = {}
        max_val = 0
        for task in tasks:
            d[task] = d.get(task, 0) + 1
            if d[task] > max_val:
                max_val = d[task]
        max_val -= 1
        idle_slots = max_val * (n + 1)
        for k, v in d.items():
            idle_slots -= min(max_val, v)
        return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
from collections import Counter
class Solution1:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks).values()
        M = max(task_counts)
        m_count = 0
        for i in task_counts:
            if i == M:
                m_count += 1
        return max(len(tasks), (M - 1) * (n + 1) + m_count)
