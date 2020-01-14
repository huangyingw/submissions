class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        region_to_parent = {}
        for region_list in regions:
            parent = region_list[0]
            for region in region_list[1:]:
                region_to_parent[region] = parent
        region1_parents = [region1]
        while region1_parents[-1] in region_to_parent:
            region1_parents.append(region_to_parent[region1_parents[-1]])
        region1_parents = set(region1_parents)
        while region2 not in region1_parents:
            region2 = region_to_parent[region2]
        return region2
