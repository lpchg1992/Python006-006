#!/usr/bin/env python
import sys
import os
import time

'''
手动编写一个daemon进程
'''

def daemonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:

        # 创建子进程
        pid = os.fork()

        if pid > 0:
            # 父进程先于子进程exit，会使子进程变为孤儿进程，
            # 这样子进程成功被init这个用户级守护进程收养
            sys.exit(0)

    except OSError as err:
        sys.stderr.write('_Fork #1 failed: {0}\n'.format(err))
        sys.exit(1)

    # 从父进程环境脱离
    # decouple from parent environment
    # chdir确认进程不占用任何目录，否则不能umount
    os.chdir("/")
    # 调用umask(0)拥有写任何文件的权限，避免继承自父进程的umask被修改导致自身权限不足
    os.umask(0)
    # setsid调用成功后，进程成为新的会话组长和新的进程组长，并与原来的登录会话和进程组脱离
    os.setsid()

    # 第二次fork
    try:
        pid = os.fork()
        if pid > 0:
            # 第二个父进程退出
            sys.exit(0)
    except OSError as err:
        sys.stderr.write('_Fork #2 failed: {0}\n'.format(err))
        sys.exit(1)

    # 重定向标准文件描述符
    sys.stdout.flush()
    sys.stderr.flush()

    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'w')

    # dup2函数原子化关闭和复制文件描述符
    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())

# 每秒显示一个时间戳
def test():
    sys.stdout.write('Daemon started with pid %d\n' % os.getpid()) 
    while True:
        now = time.strftime("%X", time.localtime())
        sys.stdout.write(f'{time.ctime()}\n') 
        sys.stdout.flush() 
        time.sleep(1)

if __name__ == "__main__":
    daemonize('/dev/null','/luopingcheng/prgtemp/1.log','/dev/null')
    test()