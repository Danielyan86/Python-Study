import unittest

import requests


class GitHubAPITest(unittest.TestCase):
    def test_event(self):
        # response = requests.get("https://api.github.com/events")
        # content = response.json()
        # for item in content:
        #     if "payload" in item:
        #         print(item['payload'])
        # self.assertEqual(payload_dic['ref_type'], "repository")
        url = "http://127.0.0.1:8000/users/"
        payload = {}
        headers = {"Authorization": "Token af60bd228881ea4e2fca375221f39627578026ff"}
        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()[0]
        print(data)
        self.assertEqual("admin", data["username"])
        self.assertEqual(True, data["is_staff"])


if __name__ == "__main__":
    unittest.main()
