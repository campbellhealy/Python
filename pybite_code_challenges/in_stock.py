# in_stock.py
'''
A simple check to see if an item is in a list or not.
It's an infinte loop that require a quit statement
Where the item is not in the list, a message is presented.
'''

IN_STOCK = ['mini', 'transit', 'doblo']

def find_car():
    while True:
        request = input('Enter a car: ')
        request = request.lower()
        if request in IN_STOCK:
            print(request)
        elif request =='quit':
            print('bye')
            break
        else:
            print('Vehicle not in stock')

find_car()