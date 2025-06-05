def find_min(lst: list):
    ans_index = 0
    answer = lst[0]

    for i in range(len(lst)):
        if lst[i] < answer:
            answer = lst[i]
            ans_index = i

    return ans_index


def find_max(lst: list):
    ans_index = 0
    answer = lst[0]

    for i in range(len(lst)):
        if lst[i] > answer:
            answer = lst[i]
            ans_index = i

    return ans_index


def selection_sorted(lst: list):
    ans = []

    for i in range(len(lst)):
        ind = find_min(lst)
        ans.append(lst.pop(ind))

    return ans
