import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.link = None
    
class SingleLinkedList:
    def __init__(self):
        self.start = None
    
    def display_list(self):
        pass
    
    def count_nodes(self):
        pass
    
    def search(self, x):
        pass
    
    def insert_at_begining(self, data):
        pass
    
    def insert_at_end(self, data):
        pass
    
    def create_list(self):
        pass
    
    def insert_before(self, data, x):
        pass
    
    def insert_after(self, data, x):
        pass
    
    def insert_at_position(self, data, k):
        pass
    
    def delete_node(self, x):
        pass
    
    def delete_first_node(self):
        pass
    
    def delete_last_node(self):
        pass
    
    def reverse_list(self):
        pass
    
    def bubble_sort_exdata(self):
        pass
    
    def bubble_sort_exlinks(self):
        pass
    
    def has_cycle(self):
        pass
    
    def find_cycle(self):
        pass
    
    def remove_cycle(self):
        pass
    
    def insert_cycle(self):
        pass
    
    def merge2(self, list2):
        pass
    
    def _merge2(self, p1, p2):
        pass
    
    def merge_sort(self):
        pass
    
    def _merge_sort_rec(self, liststart):
        pass
    
    def _divide_list(self, p):
        pass
    
##########################################################################################
list = SingleLinkedList()

list.create_list()

    
while True:
    print('1. Display List')
    print('2. Count the number of Nodes')
    print('3. Search for an element')
    print('4. Insert in Empty List/Insert in the beginning of List')
    print('5. Insert node at the end of the list')
    print('6. Insert a node before a Specified node')
    print('7. Insert a node after a specified node')
    print('8. Insert a node at a given position')
    print('9. Delete first node')
    print('10. Delete last node')
    print('11. Delete any node')
    print('12. Reverse the list')
    print('13. Bubble sort by exchange data')
    print('14. Bubble sort by exchange links')
    print('15. Merge sort')
    print('16. Insert Cycle')
    print('17. Detect Cycle')
    print('18. Remove Cycle')
    print('19. Quit')
    
option = int(input('Enter the Choice : '))

if option == 1:
    list.create_list()
elif option == 2:
    list.count_nodes()
elif option == 3:
    data = int(input('Enter the element to be searched : '))
    list.search(data)
elif option == 4:
    data = int(input('Enter the element to be inserted : '))
    list.insert_at_begining(data)
elif option == 5:
    data = int(input('Enter the element to be inserted : '))
    list.insert_at_end(data)
elif option == 6:
    data = int(input('Enter the element to be inserted : '))
    x = int(input('Enter the element after which to insert : '))
    list.insert_after(data, x)
elif option == 7:
    data = int(input('Enter the element to be inserted : '))
    x = int(input('Enter the element before which to insert : '))
    list.insert_before(data, x)
elif option == 8:
    data = int(input('Enter the element to be inserted : '))
    k = int(input('Enter the position which to insert : '))
    list.insert_at_position(data, k)
elif option == 9:
    list.delete_first_node()
elif option == 10:
    list.delete_last_node()
elif option == 11:
    data = int(input('Enter the element to be deleted : '))
    list.delete_node(data)
elif option == 12:
    list.reverse_list()
elif option == 13:
    list.bubble_sort_exdata()
elif option == 14:
    list.bubble_sort_exlinks()
elif option == 15:
    list.merge_sort()
elif option == 16:
    data = int(input('Enter the element at which the cycle has to be inserted : '))
    list.insert_cycle(data)
elif option == 17:
    if list.has_cycle():
        print('List has cycle')
    else:
        print('List does not have cycle')
elif option == 18:
    list.remove_cycle()
elif option == 19:
    sys.exit()
else:
    print('Wrong Option')
print()
    