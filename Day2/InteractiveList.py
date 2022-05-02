#!/usr/bin/python

daList = ["One","Two","Three"]

print('''
Welcome to List: /n 
1. View the List /n 
2. Add to List /n 
3. Delete from List /n 
''')

int number=(input("Enter Number:"))

listStuff(number)

def listStuff(num):
	match number:
		case 1:
			print(daList)
		case 2:
			value=input("Enter Item")
			
			for x in daList:
				if x == value:
					print("Item is already in the list")
				else:
					append.daList(value)
					print("Added Successfully!")
		case 3:
			delValue=(input("Value to delete."))
			for x in daList:
				if x == delValue:
					daList.delete(delValue)
					print("Deleted.")
				else:
					print("Value not found")
		case default:
			print("Enter a correct number")