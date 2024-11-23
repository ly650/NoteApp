import requests
from common.caseMsgLogs import info, error, case


class BusinessRe:
    @staticmethod
    def post(url, sid, user_id, body, headers=None):
        if headers is None:
            headers = {
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(user_id),
                'Content-Type': 'application/json'
            }

        info(f'request url: {url}')
        info(f'request headers: {headers}')
        info(f'request body: {body}')
        try:
            res = requests.post(url, headers=headers, json=body, timeout=5)
        except TimeoutError:
            error(f'url: {url}, requests timeout！')
            return 'Requests Timeout!'
        info(f'response code: {res.status_code}')
        info(f'response body: {res.text}')
        return res

    def get(self):
        pass
