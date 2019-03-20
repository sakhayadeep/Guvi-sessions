'''
linked list in python
'''
class node:
    def __init__(self, data = None, next_node = None, prev_node = None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def getdata(self):
        return self.data
    
    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, next_node):
        self.next_node = next_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node

class linkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = node(data)
        
        current = self.head
        if(current == None):
            self.head = new_node
        else:
            while(current.get_next() != None):
                current = current.get_next()
            current.set_next(new_node)

    def getsize(self):
        current = self.head
        size = 0
        while current:
            if current.get_next() == None:
                break
            else:
                size += 1
                current = current.get_next()

        return size

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getdata() == data:
                found = True
            else:
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        return current

    def delete(self, data = None, index = None, rindex = None):
        current = self.head
        pre = None
        found = False
    
        if(data != None):
            while current and found is False:
                if current.getdata() == data:
                    found = True
                else:
                    pre = current
                    current = current.get_next()
        
        elif(index != None):
            if index > self.getsize():
                raise IndexError("Index out of range")
            else:
                while (index-1):
                    pre = current
                    current = current.get_next()
                    index -= 1
        elif(rindex != None):
            if rindex > self.getsize():
                raise IndexError("Index out of range")
            else:
                for i in range(rindex):
                    current =  current.get_next()
                nextCurrent = self.head
                while(True):
                    pre = nextCurrent
                    nextCurrent = nextCurrent.get_next()
                    if(current.get_next() == None):
                        break
                    current = current.get_next()
                
        if current is None:
            raise ValueError("Data not in list")
        if pre is None:
            self.head = current.get_next()
        else:
            if(rindex == None):
                pre.set_next(current.get_next())
            else:
                pre.set_next(nextCurrent.get_next())

def main():
    ll = linkedList()        # create linked list

    for i in range(10):
        ll.insert(i)         # insert elememt

    try:
        ll.delete(5)         # to delete with data
        ll.delete(index=3)   # to delete with index
        ll.delete(rindex=3)  # to delete with reverse index
    except Exception as ex:
        print(ex)

    for i in range(10):
        try:
            print(ll.search(i).getdata())  # search and print if found
        except Exception as ex:
            print(ex)
            
    
if __name__ == "__main__":
    main()