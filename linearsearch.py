def linear_search(lst, target):
    for i in range(len(lst)):
        if(lst[i] == target):
            return i
    return -1
