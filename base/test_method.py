import json
import unittest
from base.demo import RunMain
from base.apisql import query


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
        self.a = query()
        self.name = self.a[0]
        self.pwd = self.a[1]
    def test_01(self):
        url = 'https://class-rd.youke100.com/class_in/admin/user/login?account={n}&password={m}&isVaildCode=false'
        url = url.format(n=self.name,m=self.pwd)
        data = {
        }
        res1 = self.run.run_main(url, "POST", json.dumps(data))
        print(res1)
        print(type(res1))
        print(res1['statusCode'])
        self.assertEqual(res1['statusCode'],0,"测试失败")

if __name__ == '__main__':
    unittest.main()
