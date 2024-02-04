# Fetch release build version
# There are the following folders with major version numbers, named as Release-x.x, for example:
# Release-1.3
# Release-1.4.3
# Release-1.4.4
# Release-2.0.1
# Release-2.1.1
# Release-3.1
# Release-12.05.1
# Release-12.05.07
# …
# Please implement the following function (Any language):
# Find the latest release version.


def find_the_latest_release(releses_list):
    latest_version = 0
    lastst_number = 0
    for item in releses_list:
        number_v = item.split("-")[1]
        number_st = [x for x in number_v if x.isdigit()]
        tmp = ""
        for num in number_st:
            tmp = tmp + int(num)
        if int(tmp) >= latest_number:
            latest_number = int(tmp)
            latest_version = number_v
    return "".join(("Release-", latest_version))


if __name__ == "__main__":
    res = find_the_latest_release(["Release-1.3", "Release-1.4.3"])
    print(res)
