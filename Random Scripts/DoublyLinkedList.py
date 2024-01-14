class Node:
    def __init__(self, data):
        # initialize a node with data and next pointer
        self.prev = None
        self.data = data
        self.next = None
    def __str__(self):
        # string representation of a node
        prev_data = self.prev.data if self.prev else 'None'
        next_data = self.next.data if self.next else 'None'
        return f'(prev = {prev_data}, {self.data}, next = {next_data})'

class DoublyLinkedList: 
    # initialize an empty doubly linked list
    def __init__(self, max_size = None):
        # head is initialized at None because the list is empty  
        self.head = None
        self.MAX_SIZE = max_size
    
    # check if the doubly linked list is empty
    def isEmpty(self):
        return self.head is None
    
    # return the node count
    def nodeCount(self):
        count = 0
        # check if the linked list is empty
        if self.isEmpty():
            return count
        # if the list is not empty, proceed
        # start at the head
        currentNode  = self.head
        while currentNode is not None:
            count += 1
            # Move to the next node
            currentNode  = currentNode.next
        return count 
  
    # check if the doubly linked list is full
    def isFull(self):
        if self.MAX_SIZE is None:
            return False
        return self.MAX_SIZE == self.nodeCount()
    
    # forward traverse the linked list
    def traverse(self):
        # check if the linked list is empty
        if self.isEmpty():
            print("Doubly linked list is empty")
            return
        # if the list is not empty, proceed
        # start at head
        print('The list is: ', end = ' ')
        currentNode = self.head
        while currentNode is not None:
                print(currentNode, end=" ")
                # visit the node pointed by next pointer until a node points to head
                currentNode = currentNode.next
        print("\n")
    # insert into an empty linked list
    def insert_node(self, data):
        # create node
        new_node = Node(data)
        # assign both pointers to None
        new_node.next = None
        new_node.prev = None
        # update the head
        self.head = new_node
        print(data, 'inserted.')
        
    # insert at the beginning of the doubly linked list
    def insert_at_beginning(self, data):
        # if the linked list is full, return OverflowError
        if self.isFull():
            print('Cannot insert any more nodes')
            return
        # insert in empty list if the linked list is empty
        if self.head is None:
            self.insert_node(data)
            return
        # create a new node
        new_node = Node(data)
        # adjust prev and next pointers
        new_node.next = self.head
        self.head.prev = new_node
        # shift head
        self.head = new_node
        print(data, 'inserted.')
        
    # insert at the end of the linked list
    def insert_at_end(self, data):
        # if the list is full, return Error
        if self.isFull():
            print('Cannot add any more nodes')
            return
        # create a new node
        new_node = Node(data)
        # if the list is empty, perform insert in an empty list
        if self.isEmpty():  
            self.insert_node(data)
            return
        # otherwise insert at the end of a doubly linked list 
        # find the end of the list
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        # adjust prev and next pointers
        temp.next = new_node
        new_node.prev = temp
        print(data, 'inserted.')

    # insert at given position
    def insert_at_position(self, data, position):
        # if the list is full, return Error
        if self.isFull():
            print('Cannot add any more nodes')
            return
        # check if position is valid
        if position <= 0:
            print("Invalid position")
            return
        # if position is 1, perform insert at beginning
        elif position == 1:
            self.insert_at_beginning(data)
            return
        # if position > number of nodes, insert at the end
        elif position > self.nodeCount():
            self.insert_at_end(data)
            return
        # proceed if the position is valid
        else:
            # create a new node
            new_node = Node(data)
            # find the given position
            temp = self.head
            for i in range(position - 1):
                temp = temp.next
            # adjust next and prev pointers
            new_node.prev = temp.prev
            temp.prev.next = new_node
            new_node.next = temp
            temp.prev = new_node
        print(data, 'inserted.')
     
    # delete from the start of the doubly linked list   
    def delete_from_start(self):
        # check if the linked list is empty
        if self.isEmpty():
            print('Cannot delete from Empty Linked List')
            return
        print('Deleting', self.head.data)
        # check if the doubly linked list has only one node
        if self.head.next == None:
            self.head = None
            return
        # else if the linked list has more than one node
        # shift the head pointer to second node
        self.head = self.head.next
        # assign the previous pointer of head to None
        self.head.prev = None
        
    # delete from the start of the doubly linked list
    def delete_at_end(self):
        # check if the linked list is empty
        if self.isEmpty():
            print('Cannot delete from Empty Linked List')
            return
        # check if the  linked list has only one element
        if self.head.next == None:
            self.delete_from_start()
            return
        # traverse to th end of the linked list
        temp = self.head
        # locate second last node
        while temp.next.next is not None:
            temp = temp.next
        print(temp.next.data,'deleted.')
        # change next pointer of second last node to None
        temp.next = None

    # delete at any given position
    def delete_at_position(self, position):
        # check if the list is empty
        if self.isEmpty():
            print('Cannot delete from Empty circular linked list')
            return
        # check if the provided position is Valid
        if position <= 0:
            print('Invalid position')
            return
        # if position is 1, perform delete from start instead
        if position == 1:
            self.delete_from_start()
            return
        # if position > number of nodes, delete the last node
        if position >= self.nodeCount():
            self.delete_at_end()
            return
        # locate the node to delete
        temp = self.head
        for i in range(position - 1):
            temp = temp.next
        # reassign the next and previous pointer
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        print(temp.next.data, 'deleted.')


# Create an instance of the DoublyLinkedList class
my_list = DoublyLinkedList()
my_list.insert_at_end('A') # A
my_list.insert_at_end('B') # A B
my_list.insert_at_end('C') # A B C
my_list.insert_at_end('D') # A B C D
my_list.traverse()  # Output:  A B C D


my_list.delete_at_position(2) # A C D 
my_list.traverse() 

my_list.delete_from_start() #  C D
my_list.traverse() 

my_list.delete_at_end() # C 
my_list.traverse() 

