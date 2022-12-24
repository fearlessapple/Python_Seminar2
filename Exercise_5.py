# Реализуйте алгоритм перемешивания списка.

import random
# my_list = ["264", "75959", "bvijsn", "efilbvdwboi4", "skjbv", "22245"]
# random.shuffle(my_list)
# print(my_list)

def list_shuffle(_list: list):
    shuffled_list = []
    temp_list = _list

    for _ in range(len(_list)):
        position = random.randint(0, len(temp_list)-1)
        shuffled_list.append(temp_list.pop(position))
    return shuffled_list

print(list_shuffle([1, 2, 8, 6, 7, 12]))    