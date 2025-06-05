def quick_sort(lst: list) -> list:
    if len(lst) < 2:
        return lst

    else:
        elem = lst[0]

        greater = []
        less = []

        for i in range(1, len(lst)):
            if lst[i] <= elem:
                less.append(lst[i])
            else:
                greater.append(lst[i])

        ans = quick_sort(less) + [elem] + quick_sort(greater)

        return ans


lst = [1, 3, 6, 8, 2, 4, 1, 5, 7]

print(quick_sort(lst))
