import unittest
import requests


class GitHubAPITest(unittest.TestCase):

    def test_event(self):
        response = requests.get("https://api.github.com/events")
        content = response.json()
        for item in content:
            if "payload" in item:
                print(item['payload'])
        # self.assertEqual(payload_dic['ref_type'], "repository")


if __name__ == '__main__':
    unittest.main()
