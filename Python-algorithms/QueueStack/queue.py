def queue(string_para):
    string_new = ''
    string_old = string_para

    while 1:
        if string_old:
            if len(string_old) == 1:
                string_new = string_new + string_old[0]
                string_old = ""
            else:
                string_new = string_new + string_old[0]
                string_old = string_old[1:]
                string_old = string_old[1:] + string_old[0]
                print string_old, string_new
        else:
            break
    return string_new


if __name__ == '__main__':
    print queue("63175892443")
