def check_lists(first_list, second_list):
    if len(first_list) > len(second_list):
        longer_list, shorter_list = first_list, second_list
    else:
        longer_list, shorter_list = second_list, first_list

    for i in range(len(longer_list) - len(shorter_list)):
        if longer_list[i,len(shorter_list)] == shorter_list:
            return True

    return False