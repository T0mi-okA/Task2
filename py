Бинарная куча
import heapq

# Создание бинарной мин-кучи
binary_heap = []
data = [5, 3, 8, 1, 2, 7]

# Добавление элементов в кучу
for item in data:
    heapq.heappush(binary_heap, item)

print("Бинарная куча после добавления элементов:", binary_heap)

# Извлечение минимального элемента
min_element = heapq.heappop(binary_heap)
print("Извлеченный минимальный элемент:", min_element)
print("Куча после извлечения:", binary_heap)

# Преобразование списка в кучу
another_list = [9, 4, 6, 2, 1]
heapq.heapify(another_list)
print("Преобразованный список в кучу:", another_list)

# Получение минимального элемента без извлечения
print("Текущий минимальный элемент:", another_list[0])

Биномиальная куча
class BinomialNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None
    
    def __str__(self):
        return f"BinomialNode(key={self.key}, degree={self.degree})"

class BinomialHeap:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None
    
    def insert(self, key, value=None):
        new_heap = BinomialHeap()
        new_heap.head = BinomialNode(key, value)
        self.union(new_heap)
    
    def union(self, other_heap):
        self.head = self._merge_heaps(self.head, other_heap.head)
        if self.head is None:
            return
        
        prev = None
        curr = self.head
        next_node = curr.sibling
        
        while next_node is not None:
            if (curr.degree != next_node.degree or 
                (next_node.sibling is not None and 
                 next_node.sibling.degree == curr.degree)):
                prev = curr
                curr = next_node
            elif curr.key <= next_node.key:
                curr.sibling = next_node.sibling
                self._link_trees(curr, next_node)
            else:
                if prev is None:
                    self.head = next_node
                else:
                    prev.sibling = next_node
                self._link_trees(next_node, curr)
                curr = next_node
            next_node = curr.sibling
    
    def _merge_heaps(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        result = None
        if head1.degree <= head2.degree:
            result = head1
            result.sibling = self._merge_heaps(head1.sibling, head2)
        else:
            result = head2
            result.sibling = self._merge_heaps(head1, head2.sibling)
        return result
    
    def _link_trees(self, parent, child):
        child.parent = parent
        child.sibling = parent.child
        parent.child = child
        parent.degree += 1
    
    def extract_min(self):
        if self.head is None:
            return None
        
        # Находим узел с минимальным ключом
        min_node_prev = None
        min_node = self.head
        curr = self.head
        prev = None
        
        while curr is not None:
            if curr.key < min_node.key:
                min_node = curr
                min_node_prev = prev
            prev = curr
            curr = curr.sibling
        
        # Удаляем минимальный узел из списка корней
        if min_node_prev is None:
            self.head = min_node.sibling
        else:
            min_node_prev.sibling = min_node.sibling
        
        # Создаем новую кучу из детей минимального узла
        child_heap = BinomialHeap()
        child = min_node.child
        while child is not None:
            next_child = child.sibling
            child.sibling = child_heap.head
            child.parent = None
            child_heap.head = child
            child = next_child
        
        # Объединяем с основной кучей
        self.union(child_heap)
        
        return min_node.key, min_node.value
    
    def find_min(self):
        if self.head is None:
            return None
        
        min_node = self.head
        curr = self.head.sibling
        
        while curr is not None:
            if curr.key < min_node.key:
                min_node = curr
            curr = curr.sibling
        
        return min_node.key, min_node.value

# Пример использования биномиальной кучи
print("\n" + "="*50)
print("БИНОМИАЛЬНАЯ КУЧА")
print("="*50)

bh = BinomialHeap()
elements = [10, 5, 15, 3, 7, 12, 1]

print("Добавляем элементы:", elements)
for elem in elements:
    bh.insert(elem)

print("Минимальный элемент:", bh.find_min()[0])

min_val = bh.extract_min()
print("Извлечен минимальный элемент:", min_val[0])
print("Новый минимальный элемент:", bh.find_min()[0])

# Добавляем еще элементы
bh.insert(2)
bh.insert(8)
print("После добавления 2 и 8, минимальный:", bh.find_min()[0])

# Извлекаем все элементы
print("\nИзвлекаем все элементы по порядку:")
while not bh.is_empty():
    min_val = bh.extract_min()
    print(min_val[0], end=" ")
print()
