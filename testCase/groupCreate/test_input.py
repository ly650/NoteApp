import unittest
import requests
from copy import deepcopy
import time
from common.generalAssert import GeneralAssert
from colorama import Fore
from business.businessRe import BusinessRe
from common.caseMsgLogs import case, info, error, class_case_decoration
from business.dataCreate import DataCreate
from common.yamlRead import YamlRead
from parameterized import parameterized


@class_case_decoration
class GroupCreateInput(unittest.TestCase):
    apiConfig = YamlRead().api_config()['group_create']
    envConfig = YamlRead().env_config()
    ga = GeneralAssert()
    re = BusinessRe()
    user_id1 = envConfig['user_id1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    url = host + apiConfig['path']
    mustKeys = apiConfig['mustKeys']
    # mustKeyItems = [[{'key': 'groupId', 'code': 400}], [{'key': 'groupName', 'code': 500}]]

    def setUp(self) -> None:
        # 用户数据清理
        pass

    @parameterized.expand(mustKeys)
    def testCase01_input_must_key_remove(self, key):
        """新增分组接口，必填项缺失"""
        info('用户A请求新增分组接口')
        group_id = str(int(time.time() * 1000))
        body = {
            "groupId": group_id,
            "groupName": 'test',
            "order": 0
        }
        body.pop(key)
        res = self.re.post(self.url, sid=self.sid1, user_id=self.user_id1, body=body)
        self.assertEqual(500, res.status_code, msg='状态码校验失败')
