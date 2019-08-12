# coding = utf-8
import random

ball_type = ["A", "B", "C", "D", "E", "F", "G"]


def prepare(n):
    balls_arr = []
    for i in range(n):
        idx = random.randint(0, 6)
        balls_arr.append(ball_type[idx])
    return balls_arr


def can_get_7_balls(lis):
    # INPUT YOUR CODES HERE
    return len(set(lis)) == len(ball_type)


if __name__ == '__main__':
    for i in range(100):
        balls = prepare(9)
        # print(balls)
        if can_get_7_balls(balls):
            print(sorted(balls))
