import pexpect as PX
import sys


def run_example():
    output = PX.run("ls -la")
    print(output)


def spawn_example():
    # 通过spqwn方法把输出写入文件
    child = PX.spawn('docker exec -it ecstatic_liskov /bin/bash')
    fout = open('mylog.txt', 'wb')
    # child.logfile = fout
    child.expect('[#$] ')
    res = child.sendline(r"free")
    # 将之前 open 的 file 对象指定为 spawn 类子程序对象的 log 文件.
    child.logfile = fout
    # 命令运行完后，expect EOF 出现，这时会将 spawn 类子程序对象的输出写入到 log 文件.
    child.expect(PX.TIMEOUT)
    # open 完文件，使用完毕后，需关闭该文件.
    fout.close()


# child.logfile = sys.stdout
# print(child.logfile)
# print(child)


if __name__ == '__main__':
    spawn_example()
