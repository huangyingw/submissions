












class SnakeGame(object):
    def __init__(self, width, height, food):

        self.rows, self.cols = height, width
        self.food = [tuple(f) for f in food]
        self.snake = {(0, 0): None}
        self.head, self.tail = (0, 0), (0, 0)
        self.moves = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

    def move(self, direction):


        new_head = (self.head[0] + self.moves[direction][0], self.head[1] + self.moves[direction][1])

        if new_head[0] < 0 or new_head[0] >= self.rows or new_head[1] < 0 or new_head[1] >= self.cols:
            return -1

        if new_head in self.snake and new_head != self.tail:
            return -1

        self.snake[self.head] = new_head
        self.head = new_head

        if len(self.snake) - 1 >= len(self.food) or new_head != self.food[len(self.snake) - 1]:
            old_tail = self.tail
            self.tail = self.snake[self.tail]
            del self.snake[old_tail]

        self.snake[self.head] = None
        return len(self.snake) - 1
