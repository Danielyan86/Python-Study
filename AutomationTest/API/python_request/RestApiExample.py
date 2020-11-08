import os

import requests


class DjangoRestApi:
    req = requests.Session()

    def get_token(self):
        # headers = {'Accept': 'application/json', 'User-Agent': 'PostmanRuntime/7.24.1'}
        data = {"username": "admin", "password": "123456"}
        url = "http://localhost:8000/get_auth_token/"
        req = self.req.post(url=url, data=data)
        print(req.text)

    def get_user_info(self):
        url = "http://127.0.0.1:8000/users/"
        req = self.req.get(url=url)
        res_json = req.json()
        print(res_json)
        assert req.status_code == 401
        # assert res_json[0]['username'] == 'admin'
        # assert res_json[0]['is_staff'] is True

    # def login_test(self):
    #     url = "http://127.0.0.1:8000/"


class GithubRestapi:
    req = requests.Session()
    url = "https://api.github.com/"

    def get_user_info(self):
        user_url = self.url + "users/Danielyan86"
        res = self.req.get(user_url)
        assert res.status_code == 200
        print(res.json())
        data = res.json()
        username = data['login']
        assert username == 'Danielyan86'

    def get_organizations(self):
        token = os.getenv("API_automation_test_token")
        print(token)
        org_url = self.url + "orgs/playpython/members"
        headers = {"Authorization": f"Token {token}"}
        res = self.req.get(org_url, headers=headers)
        members_data = res.json()
        print(members_data)
        for item in members_data:
            if "Danielyan86" == item["login"]:
                assert item["type"] == "User"


if __name__ == '__main__':
    api_test = DjangoRestApi()
    api_test.get_token()
    # api_test = GithubRestapi()
    # api_test.get_user_info()
    # api_test.get_organizations()
