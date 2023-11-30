import requests


# 发起一个get requests请求
def get_request():
    r = requests.get("https://api.github.com/")
    print(r.url)
    print(r.text)
    print(r.content)
    print(r.json())


# 给get URL传参数
def post_request():
    payload = {"key1": "value1", "key2": "value2"}
    r = requests.get("https://httpbin.org/get", params=payload)
    print(r.status_code)
    print(r.text)


def header_request():
    # 自定义headers
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
    }
    r = requests.get("https://www.bing.com/", headers=headers)
    print(r.text)


def gen():
    return {"key1": "value1", "key2": "value2"}
    return {"key3": "value3", "key4": "value4"}


if __name__ == "__main__":
    payload = {"key1": "value1", "key2": "value2"}

    r = requests.post("https://httpbin.org/post", data=gen())
    print(r.iter_content())
    r.json()

    # hooks={'response': print_url}
    # 方法定义
    def print_url(r, *args, **kwargs):
        print(r.url)

    # print_url()
    # 使用钩子
    requests.get("https://httpbin.org/", hooks={"response": print_url})
