__author__ = 'ragupta4'

import threading


def do_this():
    global x

    while x < 300:
        x +=1
    print x

def do_after():
    global x

    x = 450
    while x < 600:
        x +=1
    print x

def main():
    global x
    x = 0

    our_thread = threading.Thread(target=do_this)
    our_thread.start()
    our_thread.join()

    our_next_thread = threading.Thread(target=do_after)
    our_next_thread.start()

    # print threading.active_count()
    # print threading.enumerate()

if __name__ == "__main__":
    main()


