



class Solution:

    def findDuplicate1(self, nums):

        num_set = set()
        for num in nums:
            if num in num_set:
                return num
            else:
                num_set.add(num)

    def findDuplicate2(self, nums):

        slow = fast = temp = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow = nums[slow]
            temp = nums[temp]
            if slow == temp:
                break
        return slow
