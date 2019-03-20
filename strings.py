'''
creating a object with string and using class functions, reverse and copy
'''
class string:
    st = str()

    def __init__(self, newstring):
        self.st = newstring

    def reverse(self):
        '''
        self.st = list(self.st)
        rst = list()
        for i in range(len(self.st)-1, -1, -1):
            rst.append(self.st[i])

        self.st = "".join(rst)
        '''
        self.st = self.st[::-1]

    def copy(self):
        return self.st
        

def main():
    ob = string("Here")

    a = ob.copy()
    ob.reverse()

    print(ob.st, a)

if __name__ == "__main__":
    main()