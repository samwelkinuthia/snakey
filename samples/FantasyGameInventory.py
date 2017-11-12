def add_to_inventory(your_stuff, loot):
    print("Your current Inventory: ")
    total = 0
    for k, v in your_items.items():
        print('- ' + str(v) + ' ' + k)
        total += v
    print("Total items: " + str(total))
    print("You have slain the dragon. Deposited loot : " + str(addedItems))
    ans = input("Collect loot?(y/n): ")
    if ans == 'Y' or ans == 'y':
        #set empty dictionary to convert list
        added_items = {}

        #loop through list, push items to added_items dictionary
        for x in addedItems:
            if type(x) is str:
                added_items[x] = int(addedItems.count(x))
            else:
                raise TypeError("Value in list is an integer. Define it more")
        #add items in added items to your inventory
        for k,v in added_items.items():
            if k in your_items and type(k) is str:
                your_items[k] += v
            else:
                your_items.setdefault(k, v)
        #print out your updated inventory
        print("Your Updated Inventory: ")
        total = 0
        for k, v in your_items.items():
            print('- ' + str(v) + ' ' + k)
            total += v
        print("Total items: " + str(total))
    else:
        print("Your didn\'t add anything to your inventory: ")
#sample items
your_items = {'armor': 21, 'gold': 30, 'ruby': 20}
#sample loot
addedItems = ['silver', 'silver', 'silver', 'ruby', 'ruby', 'gold', 'gold']

add_to_inventory(your_items, addedItems)