import unittest
import requests
import time
from common.generalAssert import GeneralAssert
from colorama import Fore
from business.businessRe import BusinessRe
from common.caseMsgLogs import case, info, error, class_case_decoration
from business.dataCreate import DataCreate


@class_case_decoration
class SetNoteGroupInput(unittest.TestCase):
    ga = GeneralAssert()
    re = BusinessRe()
    user_id1 = 922061821
    sid1 = 'V02SdJIgPeHbKDhJVkgz7SPSuae7ODk00a4833ed0036f58bfd'
    host = 'http://note-api.wps.cn'
    url = host + '/v3/notesvr/set/notegroup'

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

    # @unittest.skip('下个版本的用例')
    def testCase02_input_must_key_remove(self):
        """新增分组接口，必填项缺失：groupId"""
        info('用户A请求新增分组接口')
        headers = {
            'Cookie': f'wps_sid={self.sid1}',
            'X-user-key': str(self.user_id1),
            'Content-Type': 'application/json'
        }

        group_id = str(int(time.time() * 1000))
        body = {
            "groupId": group_id,
            "groupName": 'test',
            "order": 0
        }
        body.pop('groupId')
        res = requests.post(self.url, headers=headers, json=body)
        self.assertEqual(400, res.status_code, msg='状态码校验失败')

    def testCase02_major(self):
        """获取用户分组便签的主流程"""
        info('用户A请求新增分组接口')
        group_id = str(int(time.time() * 1000))
        body = {
            "groupId": group_id,
            "groupName": 'test',
            "order": 0
        }
        self.re.post(self.url, sid=self.sid1, user_id=self.user_id1, body=body)
        note_data = DataCreate().note_create(1, user_id=self.user_id1, sid=self.sid1, group_id=group_id)

        info('请求获取用户分组便签接口')
        pass
