__author__ = 'ragupta4'

import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(2)
        print("Finsihed background file write to %s" % self.out)


def Main():
    message = raw_input("Enter a string to store:")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print("The program continue to run while it write in another thread")
    print(100+400)

    background.join()
    print "waited until thread was complete"


if __name__ == "__main__":
    Main()

