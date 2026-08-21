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
            if cmp_function(info, element) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

def is_empty(my_list):
    return my_list["size"] == 0

def size(my_list):
    return my_list["size"]

def last_element(my_list):
    return my_list["elements"]["size"]-1

def delete_element(my_list, pos)
    del my_list["elements"][pos]
    my_list["size"] -= 1
    return my_list
    
def remove_first(my_list):
    del my_list["elements"][0]
    my_list["size"] -=1
    return my_list 

def remove_last(my_list):
    del my_list["elements"][my_list["size"]-1]
    my_list["size"] -= 1
    return my_list

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list 

def change_info(my_list, new_info, pos):
    my_list["elements"][pos] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    temporal = my_list["elements"][pos_1]
    my_list["elements"][pos_1] = my_list["elements"][pos_2]
    my_list["elements"][pos_2] = temporal
    return my_list

def sub_list(my_list, pos_i, num_elements):
    newlist = new_list()
    for i in range(pos_i, pos_i + num_elements):
        insert_element(newlist, my_list["elements"][i], size(newlist))
    return newlist
