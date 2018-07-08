#用例配置部分
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           Selenium2Library
Suite Setup      Open Browser To Login Page
Suite Teardown   Close All Browsers

#变量定义部分
*** Variables ***
${LOGIN URL}      http://127.0.0.1:8086/en-gb/accounts/login/
${BROWSER}        Chrome

#测试用例部分
*** Test Cases ***
Valid Login negative case one
    Input Text  login-username   test@163.com
    Input Password       login-password  thisisatest
    Click Button         login_submit
    Page Should Not Contain  Welcome!
    Sleep  3

Valid Login negative case two
    Input Text  login-username   test@163.com
    Input Password       login-password  thisisatest2
    Click Button         login_submit
    Page Should Not Contain  Welcome!
    Sleep  3

#用户自定义关键字
*** Keywords ***
Open Browser To Login Page          #用户关键字
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Login or register | Oscar - Sandbox

