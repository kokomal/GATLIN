# coding = utf-8
import os


# 非常简单的功能，返回当前的路径
def get_location():
    return os.path.dirname(os.path.abspath(__file__))


if __name__ == '__main__':
    print(get_location())
