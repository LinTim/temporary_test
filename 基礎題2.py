# -*- coding: utf-8 -*-

def count_it(the_num):
    count = 0
    for i in range(the_num):
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            count += 1
        elif i % 3 == 0:
            pass
        elif i % 5 == 0:
            pass
        else:
            count += 1
    return count


if __name__ == '__main__':
    the_num = 15

    print(count_it(the_num))