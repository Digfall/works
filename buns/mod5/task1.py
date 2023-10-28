class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.next = None  # ссылка на следующий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def pop(self):
        """
        возвращение последнего элемента из списка с удалением его из списка
        """
        if self.end is None:
            return None

        val = self.end.data
        self.end = self.end.next
        return val

    def push(self, val):
        """
        добавление элемента val в конец списка
        """
        new_node = Node(val)
        if self.end is None:
            self.end = new_node
        else:
            new_node.next = self.end
            self.end = new_node

    def print(self):
        """
        вывод на печать содержимого стека
        """
        current = self.end
        while current is not None:
            print(current.data)
            current = current.next
