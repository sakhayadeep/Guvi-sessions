'''
Reverse a given string with recursion
'''
class strings:
    def __init__(self, string):
        self.string = string


    def reverse(self, string = None):
        if(string == None):
            string = self.string
        if(string == ""):
            return string
        else:
            return (self.reverse(string[1:]) + string[0])

def main():
    s = strings(input())
    print(s.reverse())

if __name__ == "__main__":
    main()