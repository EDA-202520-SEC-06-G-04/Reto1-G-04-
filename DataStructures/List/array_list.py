def new_list():
    newlist = {
        'elements': [], 
        'size': 0,
    }
    return newlist

def get_element(my_list, index):
    return my_list["elements"][index]

def is_present(my_list, element, cmp_function):

    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
            if keyexist:
                return keypos
    return -1

#Inicio de creación de funciones 

def add_first(my_list, element):
    
    if my_list["size"] == 0:
        my_list["elements"]= element
        
    else:
        lista_2 = []
        lista_2[0] = element
        
        my_list = my_list + lista_2
    
    my_list["size"] += 1
    
    return my_list

def add_last(my_list, element):
    
    
    if my_list["size"] == 0:
        my_list["elements"].append(element)
    
    else:
        my_list["elements"].append(element)
    
    my_list["size"] += 1
    
    return my_list

def is_empty(my_list):
    
    size = my_list["size"]
    
    if size == 0:
        rta = True
    else:
        rta = False
    
    return rta

def size(my_list):

    size = my_list["size"]
    
    return size

def first_element(my_list):
    
    return my_list["elements"][0]

    
def last_element(my_list):
    
    return my_list["elements"][-1]

def delete_element(my_list, pos):
    
    if (pos >= 0) and (pos < (my_list["size"])):
      my_list["elements"] = my_list["elements"][:pos] + my_list["elements"][pos+1:]
      
      my_list["size"] -= 1
      
      return my_list
    
    else:
        
        return my_list["elements"][pos]
    
    
def remove_first(my_list):
    
    if my_list["size"] == 0:
        element = my_list["elements"][0] 
        
    else:
        first = my_list["elements"][0]
        my_list["elements"] = my_list["elements"][1:]
        
        my_list["size"] -= 1
        
        return first

def remove_last(my_list):
    
    if my_list["size"] == 0:
        element = my_list["elements"][0] 
        
    else:
        last = my_list["elements"][-1]
        my_list["elements"] = my_list["elements"][:-1]
        
        my_list["size"] -= 1
        
        return last

def insert_element(my_list, element, pos):
    
    if my_list["size"] == 0:
        my_list["elements"] = element
    
    else:
        my_list["elements"]= my_list["elements"][:pos] + [element] + my_list["elements"][pos:]
         
    my_list["size"] += 1
        
    return my_list


def change_info(my_list, pos, new_info):

    if (pos >= 0) and (pos < (my_list["size"])):

         my_list["elements"][pos] = new_info

         return my_list
    
    else: 
        return None


def exchange(my_list, pos_1, pos_2):

    if ((pos_1 >= 0) and (pos_1 < (my_list["size"]))) and ((pos_2 >= 0) and (pos_2 < (my_list["size"]))):
        
        element_1 = my_list["elements"][pos_1]
        element_2 = my_list["elements"][pos_2]

        my_list["elements"][pos_1] = element_2
        my_list["elements"][pos_2] = element_1

        return my_list
    
    else:
        
        return None 

def sub_list(my_list, pos_i, num_elements):

    if (pos_i >= 0) and (pos_i < (my_list["size"])):
        
        final_list = pos_i + num_elements

        if final_list > my_list["size"]:
            final_list = my_list["size"]

        elements = my_list["elements"][pos_i: final_list]
        sublista = {"size": len(elements), "elements": elements}

        return sublista
    
    else: 
        return None

    

      
