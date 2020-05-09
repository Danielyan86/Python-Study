import requests


class DjangoRestApi:
    req = requests.Session()

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
        username=res.data['username']
        self.req.post(data={'username':username})


    def get_organizations(self):
        org_url = self.url + "orgs/playpython/members"
        headers = {"Authorization": "Token 13b0dccde49aa5a390d8d701602b1b503c8130da"}
        res = self.req.get(org_url, headers=headers)
        members_data = res.json()
        print(members_data)
        for item in members_data:
            if "Danielyan86" == item["login"]:
                assert item["type"] == "User"


if __name__ == '__main__':
    api_test = DjangoRestApi()
    api_test.get_user_info()
    api_test.get_user_info()
    # api_test = GithubRestapi()
    # api_test.get_organizations()
    # api_test.get_user_info()
