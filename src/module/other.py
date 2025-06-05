def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


def rec_sum(summ, lst):
    if len(lst) > 0:
        el = lst.pop()
        return rec_sum(summ, lst) + el
    else:
        return summ


def rec_count(lst):
    tmp = 0

    if len(lst) > 0:
        lst.pop()
        return rec_count(lst) + 1
    else:
        return tmp
