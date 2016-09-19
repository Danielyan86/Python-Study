Exercise problem
=====================

Create your own folder and write the program
### Basic
1. reverse a string, input:ABCDE ouput:EDCBA
2. encrypt a string, replace the letter position 3 e.g input:ABC output:DEF
3. Fibonacci function, 
4. Multiple table

### 09/19
1.写一个方法,输入文件夹路径和文件类型,统计出该文件夹下面文件个数。
e.g  input: function (path=/, type=xml )
     output: 12 xml file in path /
     
2.  从jira上面获取对应assignee 的ticket状态和个数,

建议使用requests 包, 文档:http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
注意事项:使用get方法即可完成, 不要在不清楚轻使用post,put等方法调用API,避免造成jira数据混乱!
jira API参考文档:
https://developer.atlassian.com/jiradev/jira-apis/jira-rest-apis/jira-rest-api-tutorials/jira-rest-api-example-query-issues