# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script
 
def counting(lst:list):
    """

    looks at each item an adds + 1 if it already exits, otherwise set it to 1

    """
    items = {}
    for i in lst: 
        if i in items.keys(): 
            items[i] += 1
        else:
            items[i] = 1
    return(items) 

    