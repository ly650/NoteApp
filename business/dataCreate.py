import time
import requests


class DataCreate:
    """创建用例前置和后置数据"""
    host = 'http://note-api.wps.cn'

    def note_create(self, num, user_id, sid, group_id=None, remind_time=None):
        """通用的便签新建方法"""
        note_lists = []
        for i in range(num):

            note_id = str(int(time.time() * 1000))
            headers = {  # headers 可设置成公共变量
                'Content-Type': 'application/json',
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(user_id)
            }
            # 新建便签主体接口
            url_info = self.host + '/v3/notesvr/set/noteinfo'

            if remind_time:  # 日历便签
                body = {
                    "noteId": note_id,
                    "remindTime": remind_time,
                    "remindType": 0,
                    'star': 0
                }

            elif group_id:  # 分组便签
                body = {
                    "noteId": note_id,
                    "groupId": group_id,
                    'star': 0
                }

            else:
                body = {
                    "noteId": note_id,
                    'star': 0
                }

            requests.post(url=url_info, headers=headers, json=body)

            url_content = self.host + '/v3/notesvr/set/notecontent'
            body = {
                "noteId": note_id,
                "title": 'test',
                "summary": 'test',
                "body": 'test',
                "localContentVersion": 1,
                "BodyType": 0
            }
            requests.post(url=url_content, headers=headers, json=body)
            note_lists.append(body)
