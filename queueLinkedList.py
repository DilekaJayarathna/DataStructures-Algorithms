class QueueNode:
    def __init__(self,value):
        self.qdata = value
        self.qnext = None

class Queue:
    def __init__(self):
        self.qhead = None
        self.qtail = None
        self.qsize = 0

    def isEmpty(self):
        return self.qhead == None

    def __len__(self):
        return self.qsize

    def enqueue(self,value):
        node = QueueNode(value)
        if self.isEmpty():
            self.qhead = node
            self.qtail = node
        else:
            current = self.qtail
            current.qnext = node
            self.qtail = node
        self.qsize += 1

    def dequeue(self):
        if self.isEmpty():
            print ("Can't remove from an empty queue")
        else:
            current = self.qhead
            if self.qhead is self.qtail:
                self.qhead = None
                self.qtail = None
            else:
                self.qhead = current.qnext
            self.qsize -= 1
            return current.qdata

s = Queue()
newNode = QueueNOde
