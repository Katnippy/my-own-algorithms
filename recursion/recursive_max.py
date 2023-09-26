def recursive_max(list, max=0):
    if not list:
        return max
    else:
        pop = list.pop()
        if pop > max:
            max = pop

        return recursive_max(list, max)


print(recursive_max([2, 99, 0, 2, 4948]))
