'''
Merge sort
'''
class data:
    def __init__(self, arr):
        if(type(arr) != type(list())):
            raise ValueError("List expected, instead of", type(arr))
        else:
            self.arr = arr

    def getdata(self):
        return self.arr

    def sort(self, arr = None):
        if(arr == None):
            arr = self.arr
            n = len(self.arr)
        else:
            n = len(arr)

        if(n>1):
            mid = n//2
            left = arr[:mid]
            right = arr[mid:]

            self.sort(left)
            self.sort(right)

            i = j = k = 0

            while(i < len(left) and j < len(right)):
                if(left[i] < right[j]):
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while(i < len(left)):
                arr[k] = left[i]
                i += 1
                k += 1
            
            while(j < len(right)):
                arr[k] = right[j]
                j += 1
                k += 1

def main():
    mydata = data([1,5,2,8,3,9,7])

    mydata.sort()

    print(mydata.getdata())

if __name__ == "__main__":
    main()
