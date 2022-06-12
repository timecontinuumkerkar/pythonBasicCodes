list = [1,2,3,4,5,6]

def returning_list(list):
    return [list[0], list[len(list)-1]]


print(returning_list(list))
