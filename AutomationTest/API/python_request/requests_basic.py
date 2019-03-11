import requests

# 发起一个get requests请求
r = requests.get('https://api.github.com/')
print(r.url)
print(r.text)
print(r.content)
print(r.json())

# 给get URL传参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)
print(r.status_code)
print(r.text)

# 自定义headers
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
r = requests.get("https://www.bing.com/", headers=headers)
print(r.text)


