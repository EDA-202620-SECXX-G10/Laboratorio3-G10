import random
def new_list():
    newlist ={
        'elements' : [],
        'size' : 0,
    }
    return newlist

def get_element(my_list, index):
    
    return my_list['elements'][index-1]

def is_present(my_list, element, cmp_function):
    
    size = my_list['size']
    if size > 0:
        keyexist = False 
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos + 1
    return -1

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    return my_list["elements"][0]

def last_element(my_list):
    return my_list["elements"][my_list["size"]-1]

def delete_element(my_list, pos):
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list
    
def remove_first(my_list):
    element = my_list["elements"][0]
    del my_list["elements"][0]
    my_list["size"] -= 1
    return element

def remove_last(my_list):
    element = my_list["elements"][my_list["size"]-1]
    del my_list["elements"][my_list["size"]-1]
    my_list["size"] -= 1
    return element

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list 

def change_info(my_list, pos, new_info):
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    temporal = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = temporal
    return my_list

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def sub_list(my_list, pos_i, num_elements):
    newlist = new_list()
    for i in range(pos_i, pos_i + num_elements):
        insert_element(newlist, my_list["elements"][i], size(newlist))
    return newlist