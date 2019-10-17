*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary                        # Import the test Lib Selenium2Library
Test Teardown     Close All Browsers

*** Variables ***
${LOGIN URL}      http://127.0.0.1:8086/en-gb/accounts/login/
${BROWSER}        Chrome

*** Test Cases ***
Valid Login      # Test case name
    Open Browser To Login Page      # User keyword
    Input Text  login-username   test@163.com   # use the keyword from library Selenium2Library
    Input Password       login-password  thisisatest1234
    Click Button         login_submit
    Page Should Contain  Account
    Sleep  5

*** Keywords ***
Open Browser To Login Page          # Define a user keyword
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    Login or register | Oscar - Sandbox

