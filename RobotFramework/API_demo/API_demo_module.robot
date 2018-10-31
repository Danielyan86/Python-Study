*** Settings ***
Documentation    This is a api test demo
Library  ./ApiKeywordModule/

*** Test Cases ***
Valid login api
    [Tags]    DEBUG
    ${result}=  login  test@163.com  thisisatest1234
    should be true   ${result}
    log out

Valid login api 2
    [Tags]    DEBUG
    ${result}=  login  test@163.com  thisisatest123
    should not be True   ${result}