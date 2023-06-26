#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    copy = 0
    try:
        for i in my_list:
            if copy < x:
                print(f"{x}", end="")
                copy += 1
        print()
    except (TypeError):
        pass
    return copy
