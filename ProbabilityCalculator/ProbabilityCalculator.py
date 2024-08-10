import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents.copy()
        else:
            drawn_balls = random.sample(self.contents, num_balls)
            for ball in drawn_balls:
                self.contents.remove(ball)
            return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        success = True
        for color, count in expected_balls.items():
            if drawn_balls.count(color) < count:
                success = False
                break
        if success:
            num_successes += 1

    return num_successes / num_experiments


hat = Hat(black=5, blue=4, red=2)
probability = experiment(hat=hat, expected_balls={"red": 1, "blue": 2}, num_balls_drawn=3, num_experiments=1000)
print(probability)