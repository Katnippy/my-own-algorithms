def recursive_sum(list):
    if not list:
        return 0
    else:
        pop = list.pop()
        return pop + recursive_sum(list)
    

print(recursive_sum([2, 4, 5, 9]))
