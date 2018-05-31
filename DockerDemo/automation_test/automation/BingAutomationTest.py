from selenium import webdriver

url = "http://www.bing.com"
d = webdriver.Chrome(executable_path="./chromedriver")
d.get(url)
d.close()
