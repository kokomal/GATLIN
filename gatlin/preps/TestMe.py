# coding = utf-8
import unittest

from openpyxl.compat import file

from gatlin.preps import HTMLTestRunner


class TestMeHaha(unittest.TestCase):
    def test001(self):
        print("ooii")


if __name__ == '__main__':
    print("start")
    with open('my_report.html', 'w', encoding='utf-8') as fp:
        suite = unittest.TestSuite()
        suite.addTest(TestMeHaha('test001'))
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='My unit test',
            description='This demonstrates the report output by HTMLTestRunner.'
        )
        runner.run(suite)
    print("stop")

