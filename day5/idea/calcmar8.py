def add(x,y):
    return x + y

def sub(x,y):
    return x - y

if __name__ == '__main__':
    print "In if main statement"
    import sys
    if len(sys.argv) != 3:
        print "Usage: calcmar8.py <arg1> <arg2>"
        exit()

    print add(int(sys.argv[1]),int(sys.argv[2]))