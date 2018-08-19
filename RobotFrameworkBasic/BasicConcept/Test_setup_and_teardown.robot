#用例配置部分
*** Settings ***
Documentation     Simple example using SeleniumLibrary.   #注释和说明部分
Library           SeleniumLibrary                        #调用第三方测试库Selenium2Library
Test Setup         Open Browser To Main Page
Test Teardown     Close All Browsers                      #测试结束之后执行关键字

#变量定义部分
*** Variables ***
${LOGIN URL}      http://127.0.0.1:8086/
${BROWSER}        Chrome

#测试用例部分
*** Test Cases ***
Valid Login
    Click link   login_link
    Input Text  login-username   test@163.com
    Input Password       login-password  thisisatest1234
    Click Button         login_submit
    Page Should Contain  Welcome!
    Sleep  5

Click all product
    Click link       	xpath://li/a[@href="/en-gb/catalogue/"]
    Sleep  5

#用户自定义关键字
*** Keywords ***
Open Browser To Main Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Oscar - Sandbox

