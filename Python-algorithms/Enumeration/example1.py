number_list=[]
for i in range(1,9):
    number_list.append(i)

for number in xrange(123456789, 987654322):
    flag = True
    for j in range(1, 10):
        if str(j) not in str(number):
            flag = False
            break
    if flag:
        number_string = str(number)
        if int(number_string[0:3]) + int(number_string[3:6]) == int(number_string[6:]):
            print "{0}+{1}={2}".format(number_string[0:3], number_string[3:6], number_string[6:])

