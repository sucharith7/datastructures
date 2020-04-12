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
        

    def insert_node(self,prev_node,data):
        if not prev_node:
            print("previous node is not in the list")
            return None
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        
        
    def Delete_node(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:
            self.head=cur_node.next
            cur_node=None
            return None
        prev=None
        while cur_node and cur_node.data != key:
            prev=cur_node
            cur_node=cur_node.next
        if cur_node is None:
            return None
        prev.next=cur_node.next
        cur_node=None
        
        
    def search(self,file,word):
        for key in range(len(file)):
            if file[key] == word:
                print("the element is found", key)
                return True
        else:
            return False


    def list1(self):
        file=open('machine_learning.txt','r')
        text=file.read()
        text=list(text.split())
        print(text)
        for word in text:
            self.append(word)
        self.print_list()
        word1=input("enter a word:")
        if self.search(text,word1):
            self.Delete_node(word1)
            print("removed")
            self.print_list()
        else:
            pos=int(input("pos:"))
            self.insert_index(pos,word1)
            print("added")
            self.print_list()


llist=Linked_list()
llist.list1()