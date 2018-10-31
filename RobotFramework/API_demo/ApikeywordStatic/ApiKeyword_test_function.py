import re
import requests


def get_token(req=None):
    url = "http://127.0.0.1:8086/en-gb/"
    response = req.get(url)
    if response.status_code == 200:
        pattern = r"name='csrfmiddlewaretoken' value='(\w+)'"
        reg = re.compile(pattern)
        result = reg.search(response.text)
        return result.groups()[0]


def user_login(username=None, password=None):
    req = requests.Session()
    login_url = "http://127.0.0.1:8086/en-gb/accounts/login/"

    post_data = {"csrfmiddlewaretoken": get_token(req),
                 "login-username": username,
                 "login-password": password,
                 "login-redirect_url": "",
                 "login_submit": "Log In"}
    res = req.post(url=login_url, data=post_data)
    if res.status_code == 200:
        if 'Account' in res.text:
            return True
        else:
            return False
    else:
        return False


def hello(para):
    print(para)


if __name__ == '__main__':
    print(user_login())
