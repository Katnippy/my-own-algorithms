def recursive_count(list):
    if not list:
        return 0
    else:
        list.pop()
        return 1 + recursive_count(list)
    

print(recursive_count(["penguin", "sea otter", "seal", "whale", "dolphin"]))