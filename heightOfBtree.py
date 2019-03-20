'''
Creating a binary tree, and finding it's height
'''
class node:
    def __init__(self, data = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def getdata(self):
        return self.data

    def setdata(self, data):
        self.data = data
    
    def getleft(self):
        return self.left

    def getright(self):
        return self.right

    def setleft(self, left):
        self.left = left

    def setright(self, right):
        self.right = right

class bsTree:
    def __init__(self):
        self.root = node()

    def insert(self, data):
        if(self.root.getdata() == None):
            self.root.setdata(data)
            return self.root.getdata()

        data = node(data = data)
        current = self.root
        parent = None

        while(current != None):
            if(data.getdata() > current.getdata()):
                parent = current
                current = current.getright()
            elif(data.getdata() < current.getdata()):
                parent = current
                current = current.getleft()
            else:
                raise ValueError("Cannot insert redundant values!")

        if(data.getdata() < parent.getdata()):
            parent.setleft(data)
        else:
            parent.setright(data)

        return parent.getdata()

    def getheight(self, tree = "NOT GIVEN"):
        if(tree == "NOT GIVEN"):
            tree = self.root
        
        if(tree == None):
            return 0
        else:
            left = self.getheight(tree.getleft())
            right = self.getheight(tree.getright())

            if(left > right):
                return left + 1
            else:
                return right + 1

def main():
    mytree = bsTree()

    a = list(map(int, input("Data : ").split()))

    for i in a:
        mytree.insert(i)

    print("Height : ", mytree.getheight())

if __name__=="__main__":
    main()