class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.counter = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data = self.data + [item]
            self.counter += 1
        else:
            if self.counter == 5:
                self.counter = 0
            i = (self.counter - self.capacity)
            self.counter += 1

            self.data[i] = item

    def get(self):
        return self.data



buff = RingBuffer(5)

buff.append(3)
buff.append(4)
buff.append(1)
buff.append(2)
buff.append(90)

print(buff.get())
buff.append(353)
print(buff.get())
buff.append(777)
print(buff.get())
buff.append(111)
print(buff.get())
buff.append(222)
print(buff.get())
buff.append(333)
print(buff.get())
buff.append(444)
print(buff.get())
buff.append(909090)
print(buff.get())
buff.append(66666666666)
print(buff.get())