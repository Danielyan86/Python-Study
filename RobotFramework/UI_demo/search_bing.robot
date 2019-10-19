#用例配置部分
*** Settings ***
Documentation     测试必应搜索功能   #注释和说明部分
Library           SeleniumLibrary                        #调用第三方测试库Selenium2Library
Test Teardown     Close All Browsers                      #测试结束之后执行关键字

#变量定义部分
*** Variables ***
${BING URL}      https://cn.bing.com/?mkt=zh-CN
${BROWSER}        Chrome

#测试用例部分
*** Test Cases ***
必应搜索      #测试用例名字
  Open Browser  ${BING URL}  ${BROWSER}
  Input Text    sb_form_q  极客时间
  Submit Form    sb_form   #提交表单内容
  sleep  5s