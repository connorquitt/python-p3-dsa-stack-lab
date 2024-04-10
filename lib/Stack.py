class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, item):
        if self.full() == False:
            self.items.append(item)

    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
           return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        location = 0
        if target in self.items:
            for num in reversed(self.items):
                if num == target:
                    return location
                location += 1
        else:
            return -1
