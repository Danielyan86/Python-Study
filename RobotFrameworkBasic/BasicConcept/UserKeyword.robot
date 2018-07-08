*** Settings ***
Documentation    Suite description

*** Test Cases ***
Test case one
    打印   hello world

Test case two
    User key word two   second

*** Keywords ***
打印
  [arguments]   ${arguement}
  log  ${arguement}

User key word two
  [arguments]   ${arguement}
  log  this is ${arguement}
  log  this is user keyword 2