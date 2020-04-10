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