import requests


class django_restapi:
    req = requests.Session()

    def get_user_info(self):
        url = "http://127.0.0.1:8000/users/"
        req = self.req.get(url=url)
        res_json = req.json()
        assert req.status_code == 200
        assert res_json[0]['username'] == 'xiaodong.yan'
        assert res_json[0]['is_staff'] is True

    # def login_test(self):
    #     url = "http://127.0.0.1:8000/"


class github_restapi:
    req = requests.Session()
    url = "https://api.github.com/"

    def get_user_info(self):
        user_url = self.url + "users/Danielyan86"
        res = self.req.get(user_url)
        assert res.status_code == 200
        print(res.json())

    def get_organizations(self):
        org_url = self.url + "orgs/playpython/members"
        headers = {"Authorization": "Token c2b29eca987a62cad5f803eca0a684d916c7dfa2"}
        res = self.req.get(org_url, headers=headers)
        print(res.json())



if __name__ == '__main__':
    # api_test = django_restapi()
    # api_test.get_user_info()
    api_test = github_restapi()
    api_test.get_organizations()
    api_test.get_user_info()
