import unittest
from common.caseMsgLogs import error


class GeneralAssert(unittest.TestCase):
    def http_assert(self, expect, actual):
        """
        http返回体通用的断言方法
        :param expect: dict or list，接口返回体的预期值
        :param actual: dict or list，实际结果的获取方式通常可以用 response.json()
        :return: True 断言成功，assert fail断言失败
        """
        if isinstance(expect, dict):
            self.assertEqual(len(expect.keys()), len(actual.keys()),
                             msg=f'返回体字段长度不一致，实际返回的字段有:{list(actual.keys())}')
            for k, v in expect.items():
                self.assertIn(k, actual.keys(), msg=f'{k}字段不存在于实际返回体')
                if isinstance(v, type):
                    self.assertEqual(v, type(actual[k]),
                                     msg=f'{k}字段类型与实际处理的类型不一致，实际返回的参数值: {actual[k]}')
                elif isinstance(v, list):
                    self.assertEqual(len(expect[k]), len(actual[k]), msg=f'{k}列表元素长度不一致')
                    for index in range(len(expect[k])):
                        if isinstance(expect[k][index], type):
                            self.assertEqual(expect[k][index], type(actual[k][index]),
                                             msg=f'{k}列表下的元素类型与实际返回的类型不一致')
                        elif isinstance(expect[k][index], dict):
                            self.http_assert(expect[k][index], actual[k][index])
                        else:
                            self.assertEqual(expect[k][index], actual[k][index],
                                             msg=f'{k}列表下的元素值与实际返回的值不一致')
                else:
                    self.assertEqual(v, actual[k], msg=f'{k}字段值不一致')
        else:
            # 列表结构的断言方法
            pass

    def newAssertTrue(self, expect, msg=None):
        if not expect:
            error(f'assertFail expect: {expect}')
            self.fail(msg)
