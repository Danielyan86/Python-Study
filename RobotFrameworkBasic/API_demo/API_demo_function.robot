*** Settings ***
Documentation    This is a api test demo
Library  ./ApikeywordStatic/ApiKeyword_test_function.py

*** Test Cases ***
Valid login api
    [Tags]    DEBUG
    ${result}   user login  test@163.com  thisisatest1234
    log   ${result}
    should be true  ${result}
Valid login api two
    [Tags]    DEBUG
    ${result}   user login  test@163.com  thisisatest1234
    log   ${result}
    should be true  ${result}
Valid login api three
    [Tags]    DEBUG
    ${result}   USER LOGIN  test@163.com  thisisatest1234
     log   ${result}
    should be true  ${result}
