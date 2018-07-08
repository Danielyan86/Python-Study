class stack(object):
    stack_struct = []

    def read(self):
        if self.stack_struct:
            return self.stack_struct.pop()
        else:
            return "There is no content in stack"

    def write(self, content):
        self.stack_struct.append(content)

    def empty(self):
        self.stack_struct = []

    def Judge_plalindrome(self, string):
        self.empty()
        i = 1
        for letter in string:
            if i <= len(string) / 2:
                self.write(letter)
            elif i % 2 == 0:
                right_string = string[-i:]
                break
            else:
                print(i)
                right_string = string[-i + 1:]
                break
            i += 1
        print("left string is {0}".format(self.stack_struct))
        print("right string is {0}".format(right_string))
        for letter in right_string:
            if self.read() != letter:
                return False
        return True


if __name__ == '__main__':
    stack_obj = stack()
    string = "12235111253221"
    print(stack_obj.Judge_plalindrome(string))

    string = "123454321"
    print(stack_obj.Judge_plalindrome(string))
