_author_ = 'jake'
_project_ = 'leetcode'










class PhoneDirectory(object):
    def __init__(self, maxNumbers):



        self.free = set(range(maxNumbers))

    def get(self):

        return self.free.pop() if self.free else -1

    def check(self, number):

        return number in self.free

    def release(self, number):

        self.free.add(number)
