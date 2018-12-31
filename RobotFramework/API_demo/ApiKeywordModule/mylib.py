import re
import requests


class mylib(object):

    def __init__(self):
        self.req = requests.Session()
        self._get_token()

    def _get_token(self):
        url = "http://127.0.0.1:8086/en-gb/"
        response = self.req.get(url)
        if response.status_code == 200:
            pattern = r'''name="csrfmiddlewaretoken" value="(\w+)"'''
            reg = re.compile(pattern)
            result = reg.search(response.text)
            self.token = result.groups()[0]

    def login(self, username=None, password=None):
        self._get_token()
        url = "http://127.0.0.1:8086/en-gb/accounts/login/"

        post_data = {"csrfmiddlewaretoken": self.token,
                     "login-username": username,
                     "login-password": password,
                     "login-redirect_url": "",
                     "login_submit": "Log In"}
        res = self.req.post(url=url, data=post_data)
        if res.status_code == 200:
            if 'Account' in res.text:
                return True
            else:
                return False
        else:
            return False

    def hello(self):
        print('hello')

    def log_out(self):
        log_out_url = "http://127.0.0.1:8086/en-gb/accounts/logout/"
        res = self.req.get(url=log_out_url)


if __name__ == '__main__':
    mylib_obj = mylib()
    print(mylib_obj.login("test@163.com", "thisisatest1234"))
