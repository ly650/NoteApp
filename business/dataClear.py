import time
import requests


class DataClear:
    """创建用例前置和后置数据"""
    host = 'http://note-api.wps.cn'

    def del_notes(self, user_id, sid):
        """"""
        note_ids = []
        # step1 获取首页便签，提取noteId

        # step2 获取日历便签，提取noteId

        # step3 获取分组便签，提取noteId

        # step4 循环noteId，尽量循环删除

        # step5 清空回收站
        pass
