# coding = utf-8
import random


# returns [0,1) double
def gen_random_double():
    return random.random()


def genPi():
    ins = 0
    outs = 0
    Radius = 100.0
    steps = 1000000
    for i in range(steps):
        x1 = Radius * gen_random_double()
        y1 = Radius * gen_random_double()
        if x1 * x1 + y1 * y1 <= Radius * Radius:
            ins = ins + 1
        else:
            outs = outs + 1
    return 4.0 * ins / (steps + 0.0)


if __name__ == '__main__':
    print(genPi())
