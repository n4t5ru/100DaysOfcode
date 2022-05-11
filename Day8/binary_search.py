#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me
# Script: Binary Search

class binarySearch():

    # function which uses iterate method for binary searches
    def iterateMethod(self, array, x, low, high):
        while low <= high:
            mid = int(low + (high - low)//2)

            if (array[mid]) == x:
                return mid

            elif (array[mid]) < x:
                low = mid - 1
            else:
                high = mid - 1
        return -1

    def recursiveMethod(self, array, x, low, high):

        if high >= low:
            mid = int(low + (high - low)//2)

            if array[mid] == x:
                return mid
            elif array[mid] > x:
                return self.recursiveMethod(array, x, low, mid -1)
            else:
                return self.recursiveMethod(array, x, mid+1, high)
        else:
            return -1

    # Function to create a user defined search domain / array
    def searchDomain(self, arrayLength):
        domain = []

        for i in range(arrayLength):
            domain.append(int(input('Enter Value: ')))

        return domain

    def main(self):
        menu1 = True

        while menu1:
            print('''
            Welcome to Binary Search:
            A) Iterative Method
            B) Recursive Method
            Q) Quit
            ''')

            option = input('Enter Option: ')

            # uses iterate method to do binary search
            if option == 'A':
                length = int(input('You have to enter Array Length first: '))
                
                storedArray = self.searchDomain(length)

                searchValue = int(input('Enter Search value:' ))

                result = self.iterateMethod(storedArray, searchValue, 1, len(storedArray)-1)

                if result != -1:
                    print(f'Element is present:\n  Array Value: {str(result)}\n  Normal Value: {int(result)+1}')
                else:
                    print('Value not found.')
                break
            
            # uses recursive method to do binary search
            elif option == 'B':
                length = int(input('You have to enter Array Length first: '))
                
                storedArray = self.searchDomain(length)

                searchValue = int(input('Enter Search value:' ))

                result = self.recursiveMethod(storedArray, searchValue, 1, len(storedArray)-1)

                if result != -1:
                    print(f'Element is present:\n  Array Value: {str(result)}\n  Normal Value: {int(result)+1}')
                else:
                    print('Value not found.')
                break

            elif option == 'Q':
                menu1 = False
                print('Goodbye!!')
            else:
                print('Invalid Option. Try Again!')

theSearch = binarySearch()
theSearch.main()




    