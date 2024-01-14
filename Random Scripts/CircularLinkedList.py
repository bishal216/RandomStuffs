class Node:
    def __init__(self, data):
        # initialize a node with data and next pointer
        self.data = data
        self.next = None
    def __str__(self):
        # string representation of a node
        return '('+str(self.data)+', next ='+str(self.next.data)+')'

class CircularLinkedList: 
    # initialize an empty circular linked list
    def __init__(self, max_size = None):
        # head is initialized at None because the list is empty  
        self.head = None
        self.MAX_SIZE = max_size
    
    # check if the circular linked list is empty
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
        while(True):
            count += 1
            # Move to the next node
            currentNode  = currentNode.next
            if currentNode  == self.head:
                break
        return count 
  
    # check if the circular linked list is full
    def isFull(self):
        if self.MAX_SIZE is None:
            return False
        return self.MAX_SIZE == self.nodeCount()
    
    # forward traverse the linked list
    def traverse(self):
        # check if the linked list is empty
        if self.isEmpty():
            print("Circular linked list is empty")
            return
        # if the list is not empty, proceed
        # start at head
        print('The list is: ', end = ' ')
        currentNode = self.head
        while True:
                print(currentNode, end=" ")
                # visit the node pointed by next pointer until a node points to head
                currentNode = currentNode.next
                if currentNode == self.head:
                    break
        print("\n")
    
    def reverse(self):
        # don't need to reverse if the list is empty or has only one element
        if self.isEmpty() or self.head.next == self.head:
            return
        # in case of two or more elements, reverse the list
        prev = None
        current = self.head
        next_node = None
        
        while True:
            # store the next node
            next_node = current.next
            # reverse the next pointer of the current node
            current.next = prev
            # move prevNode and currentNode one step forward
            prev = current
            current = next_node
            # check if we have reached the original head node
            if current == self.head:
                break
        # update the head node to the last node visited
        self.head.next = prev
        self.head = prev
            
    # insert into an empty linked list
    def insert_node(self, data):
        new_node = Node(data)
        new_node.next = new_node
        self.head = new_node
        print(data, 'inserted.')
    
    # insert at the beginning of the linked list
    def insert_at_beginning(self, data):
        # if the list is full, return Error
        if self.isFull():
            print('Cannot add any more nodes')
            return
        # if the list is empty, use insertion in a new node
        if self.isEmpty():  
            self.insert_node(data)
            return       
        # create a new node
        new_node = Node(data)
        temp = self.head
        # update next pointers
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head
        # update the head attribute
        self.head = new_node
        print(data, 'inserted.')

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
        # otherwise insert at the end of a circular list
        else:
            # find the end of the list
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            # adjust next pointers
            temp.next = new_node
            new_node.next = self.head
            print(data, 'inserted.')
    
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
            count = 1
            temp = self.head
            while count < position - 1:
                temp = temp.next
                count += 1
            # adjust the next pointers
            new_node.next = temp.next
            temp.next = new_node
            print(data, 'inserted at position', position,'.')
  
    def delete_from_start(self):
        # check if the linked list is empty
        if self.isEmpty():
            print('Cannot delete from Empty Linked List')
            return
        print('Deleting', self.head.data)
        # check if the circular linked list has only one node
        if self.head.next == self.head:
            self.head = None
            return
        # else if the circular linked list has more than one node
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        # adjust the next pointer of last node to second node
        temp.next = self.head.next
        # shift head to second node
        self.head = self.head.next

    def delete_at_end(self):
        # check if the linked list is empty
        if self.isEmpty():
            print('Cannot delete from Empty Linked List')
            return
        # check if the circular linked list has only one element
        if self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        # locate second last node
        while temp.next.next != self.head:
            temp = temp.next
        print(temp.next.data,'deleted.')
        # change next pointer of second last node to head
        temp.next = self.head

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
        temp = self.head
        count = 1
        while count < position - 1:
            temp = temp.next
            count += 1
        print(temp.next.data, 'deleted.')
        temp.next = temp.next.next
    
    # extract a soecific value from the circular linked list
    def extract_value(self, value):
        # check if the circular linked list is empty
        if self.isEmpty():
            print('Cannot extract from an empty circular linked list')
            return None
        # start from the head
        current = self.head
        while True:
            # if value is found, return it
            if current.data == value:
                print(current)
                return current
            # move to the next node
            current = current.next
            # if we reach head again, the value is not present in the circular linked list
            if current == self.head:
                print('Value not found in the circular linked list')
                return None

# Create an instance of the CircularLinkedList class
my_list = CircularLinkedList()
my_list.traverse()  # Output: Circular linked list is empty

# insert C to an empty linked list
my_list.insert_node("C")
my_list.traverse()
# insert A at the beginning of the circular linked list
my_list.insert_at_beginning("A")
my_list.traverse()
# insert D at the end of the circular linked list
my_list.insert_at_end("D")
my_list.traverse()
# insert B at the position 2 of the circular linked list
my_list.insert_at_position("B", 2)
my_list.traverse() # Output: The list is: (A, next=B) (B, next=C) (C, next=D) (D, next=A)

# delete at position 3 of the circular linked list
my_list.delete_at_position(3)
my_list.traverse()
# delete at the beginning of the circular linked list
my_list.delete_from_start()
my_list.traverse()
# insert D at the end of the circular linked list
my_list.delete_at_end()
my_list.traverse() # Output: A (empty list)
