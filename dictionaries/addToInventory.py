def addToInventory(inventory,addedItems):
	for i in range(len(addedItems)):
		if addedItems[i] == (addedItems[i] in inventory.keys()):
			inventory[addedItems[i]] = inventory[addedItems[i]] + 1
		else:
			inventory.setdefault(addedItems[i],0)
			inventory[addedItems[i]] = inventory[addedItems[i]] + 1
	return inventory
	

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for k,v in inventory.items():
		print(str(v) + " " + k)
		item_total = item_total + v
	print("Total number of items: " + str(item_total))


inv = {'gold coin' : 42, 'rope':1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']
inven = addToInventory(inv,dragonLoot)
displayInventory(inven)
