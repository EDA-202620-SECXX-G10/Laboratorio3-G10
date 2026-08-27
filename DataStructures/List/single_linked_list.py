import random
def new_list():
    newlist = {
        "first": None,
        "last" : None,
        "size" : 0
    }
    return newlist 

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False 
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def is_empty(my_list):
    return my_list['size'] == 0

def add_first(my_list, element):

    new_node = {'info': element, 'next': my_list['first']}

    if my_list['size'] == 0:
        my_list['last'] = new_node

    my_list['first'] = new_node
    my_list['size'] += 1

    return my_list

def add_last(my_list, element):

    new_node = {'info': element, 'next': None}

    if my_list['size'] == 0:
        my_list['first'] = new_node
    else:
        my_list['last']['next'] = new_node

    my_list['last'] = new_node
    my_list['size'] += 1

    return my_list

def size(my_list):

     return my_list['size']

def first_element(my_list):

    if my_list["size"] == 0 or my_list["first"] is None:
        return "IndexError: list index out of range"
    return my_list["first"]["info"]

def last_element(my_list):
    if my_list['size'] == 0:
        return "IndexError: list index out of range"
    return my_list['last']['info']


def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list['size']:
        raise Exception('IndexError: list index out of range')

    if pos == 0:
        my_list['first'] = my_list['first']['next']
        if my_list['size'] == 1:
            my_list['last'] = None
    else:
        prev = my_list['first']
        for _ in range(pos - 1):
            prev = prev['next']
        node_to_delete = prev['next']
        prev['next'] = node_to_delete['next']
        if pos == my_list['size'] - 1: 
            my_list['last'] = prev

    my_list['size'] -= 1
    return my_list

def remove_first(my_list):
    if my_list['size'] == 0:
        return "IndexError: list index out of range"

    element = my_list['first']['info']
    my_list['first'] = my_list['first']['next']
    my_list['size'] -= 1

    if my_list['size'] == 0:
        my_list['last'] = None

    return element


def remove_last(my_list):
    if my_list['size'] == 0:
        return "IndexError: list index out of range"

    if my_list['size'] == 1:
        element = my_list['first']['info']
        my_list['first'] = None
        my_list['last'] = None
        my_list['size'] = 0
        return element

    prev = None
    current = my_list['first']
    while current['next'] is not None:
        prev = current
        current = current['next']

    prev['next'] = None
    my_list['last'] = prev
    my_list['size'] -= 1

    return current['info']


def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list['size']:
        return "IndexError: list index out of range"

    if pos == 0:
        return add_first(my_list, element)
    if pos == my_list['size']:
        return add_last(my_list, element)

    new_node = {'info': element, 'next': None}
    prev = None
    current = my_list['first']
    count = 0
    while count < pos:
        prev = current
        current = current['next']
        count += 1

    new_node['next'] = current
    prev['next'] = new_node
    my_list['size'] += 1
    return my_list


def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list['size']:
        return "IndexError: list index out of range"

    current = my_list['first']
    count = 0
    while count < pos:
        current = current['next']
        count += 1

    current['info'] = new_info
    return my_list


def exchange(my_list, pos1, pos2):
    if (pos1 < 0 or pos1 >= my_list['size'] or
        pos2 < 0 or pos2 >= my_list['size']):
        return "IndexError: list index out of range"

    if pos1 == pos2:
        return my_list

    current1 = my_list['first']
    count1 = 0
    while count1 < pos1:
        current1 = current1['next']
        count1 += 1

    current2 = my_list['first']
    count2 = 0
    while count2 < pos2:
        current2 = current2['next']
        count2 += 1

    current1['info'], current2['info'] = current2['info'], current1['info']
    return my_list


def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list['size']:
        return "IndexError: list index out of range"

    newlist = new_list()
    current = my_list['first']
    count = 0
    while count < pos:
        current = current['next']
        count += 1

    sub_count = 0
    while current is not None and sub_count < num_elements:
        add_last(newlist, current['info'])
        current = current['next']
        sub_count += 1

    return newlist