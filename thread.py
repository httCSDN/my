import  time
import  _thread
import threading
# """
# 创建两个时间循环，一个睡眠4秒，一个睡眠2秒
# """
# def loop0():
#     print("start loop 0 at: %s"%time.ctime())
#     time.sleep(4)
#     print("loop 0 done at: %s" % time.ctime())
#
# def loop1():
#     print("start loop 1 at: %s" % time.ctime())
#     time.sleep(2)
#     print("loop 1 done at: %s" % time.ctime())
# def main():
#     print("starting at: %s" % time.ctime())
#     """
#     派生一个新的线程，他的参数包括函数（对象）、函数参数以及可选的关键字参数
#     """
#     _thread.start_new_thread(loop0,())
#     _thread.start_new_thread(loop1,())
#     """
#     暂停5秒，原因是因为我们的Loop0函数暂停了4秒，小于4秒会出现无法输入Loop 0 done...
#     """
#     time.sleep(5)
#     print("all DONE at:%s" % time.ctime())
"""
优化
"""

class Mythread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self) :
        self.func(*self.args)




loops=[4,2]
def loop(nloop,nsec):
    print("start loop %s at: %s" % (nloop,time.ctime()))
    time.sleep(nsec)
    print("loop %s done at: %s" % (nloop,time.ctime()))
def main():
    print("starting at: %s" % time.ctime())
    threads=[]
    nloops=range(len(loops))
    for i in range(len(loops)):
        # t=threading.Thread(target=loop,args=(i,loops[i]))
        t=Mythread(loop,(i,loops[i]),loops._name_)
        threads.append(t)
    for i in nloops:
        threads[i].start()




    for i in nloops:
        threads[i].join()
    print("all DONE at:%s" % time.ctime())
if __name__ == '__main__':
    main()