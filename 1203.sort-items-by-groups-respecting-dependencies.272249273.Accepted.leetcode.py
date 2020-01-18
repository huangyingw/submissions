from collections import defaultdict


class Solution(object):
    def sortItems(self, n, m, group, beforeItems):
        def top_sort(map_to_after, before_count):
            no_before = {i for i, count in before_count.items() if count == 0}
            result = []
            while no_before:
                i = no_before.pop()
                result.append(i)
                for after in map_to_after[i]:
                    before_count[after] -= 1
                    if before_count[after] == 0:
                        no_before.add(after)
            return result if len(result) == len(before_count) else []
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        group_items = defaultdict(set)
        for item, gp in enumerate(group):
            group_items[gp].add(item)
        between_groups_after = defaultdict(set)
        groups_before_count = {gp: 0 for gp in range(m)}
        ordered_groups = {}
        for gp, items in group_items.items():
            within_group_after = defaultdict(set)
            items_before_count = {item: 0 for item in items}
            for item in items:
                for before_item in beforeItems[item]:
                    if before_item in items:
                        within_group_after[before_item].add(item)
                        items_before_count[item] += 1
                    else:
                        if group[item] not in between_groups_after[group[before_item]]:
                            groups_before_count[group[item]] += 1
                            between_groups_after[group[before_item]].add(group[item])
            ordered_items = top_sort(within_group_after, items_before_count)
            if not ordered_items:
                return []
            ordered_groups[gp] = ordered_items
        group_ordering = top_sort(between_groups_after, groups_before_count)
        if not group_ordering:
            return []
        result = []
        for gp in group_ordering:
            if gp in ordered_groups:
                result += ordered_groups[gp]
        return result
