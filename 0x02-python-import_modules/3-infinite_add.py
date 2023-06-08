#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    count = len(argv) - 1
    for i in range(count):
        sum = sum + int(argv[i + 1])
    print("{:d}".format(sum))
        
