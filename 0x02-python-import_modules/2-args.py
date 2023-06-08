#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = len(sys.argv) - 1
    if count == 0:
        print(count, "arguments.")
    elif count == 1:
        print(count, "argument:")
        for i in range(1, count + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
    else:
        print(count, "arguments:")
        for i in range(1, count + 1):
            print("{:d}: {}".format(i, sys.argv[i]))
