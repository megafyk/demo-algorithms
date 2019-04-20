class MyQueue(object): 
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
        print('Enqueued.')
    
    def dequeue(self):
        self.items.pop(0)
        print('Dequeued.')

    def size(self):
        len(self.items)
