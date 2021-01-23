#用例配置部分
*** Settings ***
Documentation     Simple example using SeleniumLibrary.   #注释和说明部分
Library           SeleniumLibrary                        #调用第三方测试库Selenium2Library
Test Teardown     Close All Browsers                      #测试结束之后执行关键字

#变量定义部分
*** Variables ***
${LOGIN URL}      http://127.0.0.1:8080/en-gb/accounts/login/
${BROWSER}        Chrome

#测试用例部分
*** Test Cases ***
Valid Login      #测试用例名字
    Open Browser To Login Page      #调用用户自定义关键字
    Input Text  login-username   test@163.com   #调用第三方库关键字并传入参数
    Input Password       login-password  thisisatest1234
    Click Button         login_submit
    Page Should Contain  Account
    Sleep  5             #系统关键字

#用户自定义关键字
*** Keywords ***
Open Browser To Login Page          #用户关键字
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Login or register | Oscar - Sandbox

