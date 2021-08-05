class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    #  returns the length of array
    def len(self):
        return self.length

    # returns the element of index
    def get(self, index):
        try:
            return self.data[index]
        except KeyError:
            raise IndexError("List index out of range")

    # adds element to array
    def append(self, item):
        self.data[self.length]=item
        self.length += 1

    # removes and returns the last element
    def pop(self):
        popped_item=self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return popped_item

    # removes the element of index, returns nothing
    def remove(self, index):
        if index<0 or index>=self.length:
            raise IndexError("List index out of range")
        else:
            item=self.data[index]
            for i in range(index, self.length-1):
                self.data[i]=self.data[i+1]
            del self.data[self.length-1]
            self.length-=1


myArr= Array()
myArr.append(12)
myArr.append(1)
myArr.append(-2)
myArr.append(-5)
myArr.append(10)
print(myArr.data)
print(myArr.data)
print(myArr.get(1))