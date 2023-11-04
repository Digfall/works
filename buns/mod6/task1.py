class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.data
            current = current.next
            i += 1
        return None

    def remove(self, index):
        if index < 0:
            return
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        current = self.head
        i = 0
        while current and i < index - 1:
            current = current.next
            i += 1
        if current and current.next:
            current.next = current.next.next

    def insert(self, n, val):
        if n <= 0:
            self.push(val)
        else:
            new_node = Node(val)
            current = self.head
            i = 0
            while current and i < n - 1:
                current = current.next
                i += 1
            if current:
                new_node.next = current.next
                current.next = new_node

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

my_list = LinkedList()
my_list.push(1)
my_list.push(2)
my_list.push(3)

print("Итерация по списку:")
for item in my_list:
    print(item)

print("Получение элементов по индексу:")
print(my_list.get(0))  # 1
print(my_list.get(1))  # 2
print(my_list.get(2))  # 3

my_list.remove(1)
print("Список после удаления элемента по индексу 1:")
for item in my_list:
    print(item)

my_list.insert(1, 4)
print("Список после вставки элемента 4 на позицию 1:")
for item in my_list:
    print(item)
