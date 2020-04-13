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