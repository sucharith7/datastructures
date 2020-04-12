class Node():
    
    def __init__(self,data):
        self.data=data
        self.next=None


class Linked_list():

    def __init__(self):
        self.head=None


    def printList(self):
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
        
        
    def insertIndex (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        index1 = 0
        last_node = self.head
        while index1 < index-1 and last_node is not None:
            last_node = last_node.next
            index1 = index1+1
        if last_node is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.next = last_node.next
            last_node.next = new_node
        
        
    def insertNode(self,prev_node,data):
        if not prev_node:
            print("previous node is not in the list")
            return None
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
