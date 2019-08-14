# coding = utf-8


def hannoi(nDisks, A, B, C):
    if len(nDisks) == 1:
        print("moving No#", nDisks[0], "from ", A, "to", C)
        return
    hannoi(nDisks[0:-1], A, C, B)
    hannoi([nDisks[-1]], A, B, C)
    hannoi(nDisks[0:-1], B, A, C)


if __name__ == '__main__':
    hannoi([1, 2, 3, 4, 5], 'A', 'B', 'C')
