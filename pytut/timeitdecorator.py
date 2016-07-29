__author__ = 'ragupta4'

import time

def timeit(function):
    def tt(*args, **kwargs):
        st = time.time()
        result = function(*args, **kwargs)
        et = time.time()

        timetaken = et - st
        print "time taken is %s" %(timetaken)
        return result

    return tt

@timeit
def foo(x):
    time.sleep(x)
    return x

if __name__ == "__main__":
    print foo(2)

