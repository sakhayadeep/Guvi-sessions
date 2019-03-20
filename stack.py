'''
Implementation of stack in python
'''
class stack:
    st = list()

    def push(self, i):
        self.st.append(i)
        print("pushed : ", i)

    def pop(self):
        if(self.st):
            print("popped : ", self.st.pop())
        else:
            print("nothing to pop!!") 

def main():
    ll = stack()

    for i in range(3):
        x = (i+1)*10
        ll.push(x)

    print()

    for i in range(4):
        ll.pop()

if __name__ == "__main__":
    main()