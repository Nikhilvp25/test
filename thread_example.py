###
from time import sleep
from threading import *


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(0.2)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(0.2)


t1 = Hello()
t2 = Hi()

#inhertence

#t1.run()
#t2.run()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("bye")


