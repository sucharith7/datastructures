class Node():
    
    def __init__(self,data):
        self.data=data
        self.next=None


class Linked_list():

    def __init__(self):
        self.head=None


    def print_list(self):
    	cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next


    def append(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return None
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
        

    def prepend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
        
    def insert_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        index = 0
        last_node = self.head
        while index < index-1 and last_node is not None:
            last_node = last_node.next
            index = index+1
        if last_node is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.next = last_node.next
            last_node.next = new_node
