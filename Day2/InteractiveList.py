#!/usr/bin/python

daList = ["One","Two","Three"]
looper=True

while looper==True:
	print('''Welcome to List: \n 1. View the List \n 2. Add to List \n 3. Delete from List \n 4. Exit\n''')

	numbr=(input("Enter Number: "))

	if numbr=='1':
		print(daList)

	elif numbr=='2':
		value=input("Enter Item: ")
		
		if value in daList:
			print("\nItem is already in the list\n")

		else:
			daList.append(value)
			print("\nAdded Successfully!\n")

	elif numbr=='3':
		delValue=(input("Value to delete: "))

		if delValue in daList:
			daList.remove(delValue)
			print("\nDeleted.\n")

		else:
			print("\nValue not found\n")
	
	elif numbr=='4':
		looper=False

	else:
		print("Enter a correct number")

