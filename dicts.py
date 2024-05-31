def create_inventory(items):
    new_dict=dict()
    new_items=set(items)
    for i in new_items:
        new_dict[i]=items.count(i)
    return new_dict
        


def add_items(inventory, items):
    for key in set(items):
        if key in inventory.keys():
            inventory[key]=inventory[key]+items.count(key)
        else:
            inventory[key]=items.count(key)
    return inventory


def decrement_items(inventory, items):

    for key in set(items):
        inventory[key] = inventory[key] - items.count(key) if items.count(key) < inventory[key] else 0

    return inventory

def remove_item(inventory, item):
    if item in inventory.keys():
        del inventory[item]
    return inventory


def list_inventory(inventory):
    item=""
    for key in inventory:
        if inventory[key]==0:
            item+=key
    del inventory[item]
    new_inventory=inventory.items()
    return list(new_inventory)

