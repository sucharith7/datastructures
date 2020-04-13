def sort(self,list1):
        sort_list = []
        while list1:
            smallest = min(list1)
            sort_list.append(smallest)
            list1.pop(list1.index(smallest))
        return sort_list


    def insertPos(self,list,number):
        for index1 in range(0,len(list)):
            if list[index1]>number:
                index=index1
                break
        list = list[:index1] + [number] + list[index1:]
        return list


     def list2(self):
        import re
        file=open('linkedlist.txt','r')
        text=file.read()
        text = re.findall('[0-9]+', text)
        print(text)
        for index in range(0, len(text)): 
            text[index] = int(text[index])
        text=self.sort(text)
        print(text)
        number=int(input("number:"))
        if self.search(text,number):
            self.deleteNode(number)
            print("removed")
            self.printList()
        else:
            finallist=self.insertPos(text,number)
            return finallist
    
    
llist=Linked_list()
llist.list2()