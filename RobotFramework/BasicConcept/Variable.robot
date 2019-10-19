*** Settings ***
Library       OperatingSystem
Resource     userdata.robot

# 变量定义部分变量的作用域是当前整个文件
*** Variables ***
${MESSAGE}    Hello, world!    #定义一个字符串
${integer}   ${3}              #定义一个整数
@{list}   how   are   you  ${MESSAGE}   #定义一个列表数据
${platform}  oracel

*** Test Cases ***
My Test
    Log    ${MESSAGE}    #打印一个字符串
    log    ${integer}    #打印一个整数


    set global variable   ${MESSAGE2}  你好     #通过RF内建关键字定义全局变量
    log  ${MESSAGE2}

    ${MESSAGE3}  set variable    ${MESSAGE2}, world!  #设置局部变量
    My Keyword   /Users/admin/PycharmProjects/Python-Study/RobotFramework/

    log  ${true}

    &{dict}    Create Dictionary    first=1    second=${2}    ${3}=third  #定义一个字典
    log   ${dict.first}                                                   #打印字典第一个元素


For loop                      #使用for循环打印列表
    :FOR    ${var}    IN    @{list}
    \    Log    ${var}
    Log   @{list}[1]
    log  ${MESSAGE2}

Another Test
    Should Be Equal    ${MESSAGE}    Hello, world!  # 使用内建关键字断言
    log   ${resourcevar}                            # 打印从另外一个文件引入的变量

Last Test
    I connet "${platform}" as user        # 使用变量替换关键字一部分

*** Keywords ***
My Keyword
    [Arguments]    ${path}
    Directory Should Exist    ${path}

I connet "${platform}" as user
   Log   ${platform}