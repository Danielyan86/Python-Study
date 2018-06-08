import sys, os

# sys.path.append(os.getcwd())
# print(sys.path)
from ApiKeywordModule.mylib import mylib


class ApiKeywordModule(mylib):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def user_print(self, information):
        print(information)
