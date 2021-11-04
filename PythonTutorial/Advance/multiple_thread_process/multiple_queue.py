import threading
from queue import Queue

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
    q = Queue()

    def __init__(self):
        self.req = requests.Session()

    def get_user_list(self):
        url = "https://api.github.com/orgs/PlayPython/members?access_token=376d764af54ded124fe3f241309e090c5b58b18e"
        res = self.req.get(url)
        self.user_urls = [item['url'] for item in res.json()]

    def one_thread_get_public_repos(self):
        res_list = []
        for url in self.user_urls:
            res = self.req.get(url + "?access_token=376d764af54ded124fe3f241309e090c5b58b18e")
            res_list.append(res.json()['public_repos'])
        print(res_list)

    def get_function(self, url):
        print(url)
        res = self.req.get(url + "?access_token=376d764af54ded124fe3f241309e090c5b58b18e")
        print(res.json()['public_repos'])
        self.q.put(res.json()['public_repos'])

    def multiple_thread_get_public_repos(self):
        threads = []
        for url in self.user_urls:
            threads.append(threading.Thread(target=self.get_function, args=(url,)))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def read_queue_write_to_file(self):
        while not self.q.empty():
            print(self.q.get())
            # print(q.get())


if __name__ == '__main__':
    spider_inst = spider()
    spider_inst.get_user_list()
    # spider_inst.one_thread_get_public_repos()

    spider_inst.multiple_thread_get_public_repos()
    spider_inst.read_queue_write_to_file()
