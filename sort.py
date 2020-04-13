def sort(self,list1):
        sort_list = []
        while list1:
            smallest = min(list1)
            sort_list.append(smallest)
            list1.pop(list1.index(smallest))
        return sort_list