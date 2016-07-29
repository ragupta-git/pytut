__author__ = 'ragupta4'


def check2power(x):
    y = x
    if x%2 != 0:
        print "Not in Series"

    flag = True

    while x >=2:
        if x%2 != 0:
            print "%s Not in Series" %(y)
            flag = False
            break

        x = x/2

    if flag: print "%s In Series" %(y)

if __name__ == "__main__":
    check2power(2)
    check2power(22)
    check2power(16)
