class move_forward_position:
    def __init__(self, string):
        self.string = string

    def move_forward_two_position(self):
        print 'original string: ' + self.string
        new_string = ''
        for i in self.string.split():
            print i
            j = ord(i) + 2
            new_string = new_string + chr(j)
        print 'new string: ' + new_string
        return new_string

move = move_forward_position('m a p').move_forward_two_position()
print move