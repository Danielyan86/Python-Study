def queue(string_para):
    counter = 1
    string_new = ''
    string_old = string_para

    while 1:
        if string_old:
            if counter == 1:
                string_new = string_new + string_old[0]
                string_old = string_old[1:]
                counter = 0
            elif counter == 0:
                string_old = string_old[1:] + string_old[0]
                counter = 1
            print string_old, string_new
        else:
            break
    return string_new


if __name__ == '__main__':
    print queue("631758924")