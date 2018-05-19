from queue import Queue
from github import Github
import requests


def queue_basic():
    q = Queue()

    for i in range(3):
        print("put the element in queue")
        print(i)
        q.put(i)

    while not q.empty():
        print("get the element from queue")
        print(q.get())


class spider:
    def get_item(self):
        pass

    def read_and_write_to_file(self):
        pass


if __name__ == '__main__':
    # queue_basic()
    # or using an access token
    # g = Github("97c10cdf15ef4442463bc4aad511e234c5943932")
    # Github Enterprise with custom hostname
    # g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

    # Then play with your Github objects:
    # url = "https://api.github.com/user/orgs?access_token=97c10cdf15ef4442463bc4aad511e234c5943932"
    url = "https://api.github.com/orgs/PlayPython/members?access_token=97c10cdf15ef4442463bc4aad511e234c5943932"
    req = requests.Session()
    res = req.get(url)
    print(
        res.json())
    for item in res.json():
        print(item)
