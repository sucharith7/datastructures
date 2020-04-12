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
