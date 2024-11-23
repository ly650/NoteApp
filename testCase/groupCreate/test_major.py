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
class GroupCreateMajor(unittest.TestCase):
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

    def testCase01_major(self):
        """新增分组接口，主流程：用户新增分组"""
        info('用户A请求新增分组接口')
        group_id = str(int(time.time() * 1000))
        body = {
            "groupId": group_id,
            "groupName": 'test',
            "order": 0
        }
        res = self.re.post(self.url, sid=self.sid1, user_id=self.user_id1, body=body)
        expect = {
            'responseTime': int,
            'updateTime': int
        }
        self.assertEqual(200, res.status_code, msg='状态码校验失败')
        self.ga.http_assert(expect, res.json())

        info('请求获取用户分组列表信息，进行数据源的校验')

        get_url = self.host + '/v3/notesvr/get/notegroup'
        body = {'excludeInValid': True}
        res = self.re.post(url=get_url, sid=self.sid1, user_id=self.user_id1, body=body)
        self.assertTrue(len(res.json()['noteGroups']) == 1)
        self.assertTrue(res.json()['noteGroups'][0]['groupId'] == group_id)
