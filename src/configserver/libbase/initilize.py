#coding=utf-8
from multiprocessing import Process,Pipe
from check import check
from mod_config import setConfig
import sys,os

class global_env():
    def __init__(self):
        self.message_send,self.message_recv =  self.pipeInit()

    def pipeInit(self):
        send,recv = Pipe()
        return send,recv
    def __getattr__(self,name):
        print "not found"
        self.atr = None



g = global_env()

def initlize():
    if os.getuid() != 0:
        print "current user is not root , please change it .........."
        sys.exit(100)

    if not check():
       print "....something wrong happens , please rapair it"
       sys.exit(100)

    init_syspath()


    # 初始化全局变量g

def init_syspath():
    """
    增加 g.path 到 /etc/profile
    """
    PATH=r"/etc/profile"
    if not g.name and not g.path:
        print "not found g.name and g.path ,please set it "
        sys.exit(100)
    astr = "export %s=%s\n"%(g.name,g.path)
    f = open(PATH,'r')
    op = f.readlines()
    tag = True
    for line in op:
        if g.name in line :
            op.remove(line)
            tag = False
    f.close()

    if  tag:
        f = open(PATH,'w')
        op.append(astr)
        f.writelines(op)
        f.close()



def init_confservername():
    """
    想不出来怎么实现，难道利用shell工具
    """
    pass

if __name__ == "__main__":
    initlize()
