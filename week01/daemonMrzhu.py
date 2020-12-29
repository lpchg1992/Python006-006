#!/usr/bin/python
# coding:utf8

import sys
import os
import time
import json
import signal
import fcntl
import atexit
import threading
import multiprocessing as mulp

from Crypto import Random


agent_logger = MLogging.Logging(setting.AGENT_CONF['LOG'],).logger


class deamon(object):
    def __init__(self, **kwargs):
        self.stdin = '/dev/null'
        self.stderr = kwargs.get('stderr', 'log/mpd_err.log')
        self.rabbitmqlog = kwargs.get('rabbitmqlog', 'log/rabbitmq.log')
        self.pidfile = kwargs.get('pidfile', 'log/mpd.pid')
        self.lockfile = kwargs.get('lockfile', 'log/mpd')
        self.workproc = kwargs.get('workproc')
        self.procn = len(self.workproc)

    def mydeamon(self):
        try:
            pid = os.fork()
            if pid > 0:
                os._exit(0)
        except OSError, e:
            raise Exception, "fork error: %s [%d]" % (e.strerror, e.errno)
            sys.exit(1)

        os.setsid()
#        os.chdir('/')
        os.umask(0)

        try:
            pid = os.fork()
            if pid > 0:
                os._exit(0)
        except OSError, e:
            raise Exception, "fork error: %s [%d]" % (e.strerror, e.errno)
            sys.exit(1)

        self.isrun()

        sys.stdout.flush()
        sys.stderr.flush()
        si = open(self.stdin, 'r')
        se = open(self.stderr, 'a+', 0)

        os.dup2(si.fileno(), sys.stdin.fileno())
        os.dup2(se.fileno(), sys.stderr.fileno())

        pid = str(os.getpid())
        pidf = open(self.pidfile, 'w+', 0)
        pidf.write(pid)
        pidf.close()

        agent_logger.info("==========start workers %s ============" %
                          time.strftime("'%Y-%m-%d %X'", time.localtime()))
        self.getworkqueue()

        atexit.register(self.delpid)
        atexit.register(self.dellock)
        signal.signal(signal.SIGTERM, self.sig_clean)

    def isrun(self):
        self.lockf = open(self.lockfile, 'w')
        try:
            fcntl.lockf(self.lockf, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except IOError, e:
            print "mpd is running......"
            sys.exit(1)

    def delpid(self):
        try:
            os.remove(self.pidfile)
        except OSError:
            pass

    def dellock(self):
        self.lockf = open(self.lockfile, 'w')
        fcntl.lockf(self.lockf, fcntl.LOCK_UN)
        try:
            os.remove(self.lockfile)
        except OSError:
            pass

    def sig_clean(self, num, obj):
        while True:
            if self.pqueue.empty() > 0:
                sys.exit(0)
            else:
                spid = self.pqueue.get()
                os.kill(spid, signal.SIGTERM)

    def mltproc(self):
        self.pqueue = mulp.Queue()
        workers = []
        for i in xrange(0, self.procn, 1):
            p = mulp.Process(target=self.run)
            workers.append(p)
            p.start()
            self.pqueue.put(p.pid)
            time.sleep(1)
        for j in workers:
            j.join()

#    def worker(self):
#        self.pqueue.put(os.getpid())
#        self.run()

    def start(self):
        self.mydeamon()
        self.mltproc()

    def stop(self):
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except IOError:
            pid = None
        if not pid:
            print "pidfile %s does not exist,Process maybe not running..." % self.pidfile
            return
        self.dellock()
        self.delpid()
        try:
            while 1:
                os.kill(pid, signal.SIGTERM)
                time.sleep(1)
        except OSError, err:
            err = str(err)
            if err.find("No such process") > 0:
                sys.exit(0)
            else:
                print err
                sys.exit(1)

    def restart(self):
        self.stop()
        time.sleep(1)
        self.start()

    def getworkqueue(self):
        pass

    def run(self):
        pass
