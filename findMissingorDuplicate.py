'''
finding missing or duplicate value wit time complexity O(1)
'''
class data:
    def __init__(self, arr):
        data = dict()
        temp = list()
        low = 0
        high = len(arr)-1
        while(low < high):
            if(arr[low] + 1 != arr[low+1]):
                data["None"] = arr[low] + 1
            if(arr[low] not in temp):
                data[str(arr[low])] = arr[low]
                temp.append(arr[low])
                low += 1
            else:
                data['dup'] = arr[low]
                low += 1
        self.data = data                

    def findMissing(self):
        return self.data.get("None")
    
    def findDuplicate(self):
        return self.data.get("dup")


def main():
    mydata = data([1,2,3,4,6,7,8,9])
    mydata2 = data([1,2,3,3,4,5,6,7])

    print(mydata.findMissing())

    print(mydata2.findDuplicate())

if __name__ == "__main__":
    main()