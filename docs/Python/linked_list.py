class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def search_target(self, data):
        if self.size == 0:
            return None

        cur = self.head
        pos = 0
        if cur.data == data:
            return cur.data, pos

        while cur.next:
            cur = cur.next
            pos += 1
            if cur.data == data:
                return cur.data, pos
        return None

    def remove(self, data):
        if self.size == 0:
            return None

        cur = self.head
        if cur.data == data:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = cur.next
            self.size -= 1
        else:
            while cur.next:
                bef = cur
                cur = cur.next
                if cur.data == data:
                    if self.tail == cur:
                        self.tail = bef
                    else:
                        bef.next = cur.next
                    self.size -= 1
                    return cur.data

    def reverse(self):
        prev = None
        cur = self.head
        self.head = self.tail

        while cur.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        self.head = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def search_target(self, data):
        if self.size == 0:
            return None

        cur = self.head
        pos = 0
        if cur.data == data:
            return cur.data, pos

        while cur.next:
            cur = cur.next
            pos += 1
            if cur.data == data:
                return cur.data, pos
        return None

    def remove(self, data):
        if self.size == 0:
            return None

        cur = self.head
        if cur.data == data:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = cur.next
            self.size -= 1
            return cur.data
        else:
            while cur.next:
                bef = cur
                cur = cur.next
                if cur.data == data:
                    if self.tail == cur:
                        self.tail = bef
                        bef.next = None
                    else:
                        bef.next = cur.next
                    self.size -= 1
                    return cur.data
        return None

    def reverse(self):
        prev = None
        cur = self.head
        self.tail = self.head
        while cur.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def append(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        return new_node.data

    def search_target(self, target):
        if self.size == 0:
            return None
        cur = self.head
        pos = 0
        if cur.data == target:
            return cur.data, pos

        while cur.next:
            pos += 1
            cur = cur.next
            if cur.data == target:
                return cur.data, pos
        return None

    def remove(self, data):
        if self.size == 0:
            return None

        cur = self.head
        if cur.data == data:
            if self.size == 1:
                self.head = None
                self.tail = None
                self.size -= 1
            else:
                self.head = self.head.next
                self.size -= 1
            return cur.data
        else:
            while cur.next:
                bef = cur
                cur = cur.next
                if cur.data == data:
                    if cur == self.tail:
                        self.tail = bef

                    bef.next = cur.next
                    self.size -= 1
                    return cur.data

        return None

    def reverse(self):
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.size = 0
#
#     def append(self, data):
#         new_node = Node(data)
#         if self.size == 0:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.size += 1
#
#     def print_list(self):
#         if self.size == 0:
#             return None
#
#         cur = self.head
#         while cur:
#             print(cur.data)
#             cur = cur.next
#
#     def search_target(self, target):
#         cur = self.head
#         pos = 0
#         if cur.data == target:
#             return cur.data, pos
#
#         while cur.next:
#             pos += 1
#             cur = cur.next
#             if cur.data == target:
#                 return cur.data, pos
#         return None
#
#     def reverse(self):
#         prev = None
#         cur = self.head
#         self.tail = self.head
#         while cur:
#             next = cur.next
#             cur.next = prev
#             prev = cur
#             cur = next
#         self.head = prev
#
#     def remove(self, target):
#         if self.size == 0:
#             return None
#
#         bef = self.head
#         cur = self.head
#
#         if target == cur.data: # 삭제하려는 노드가 첫번째 노드일때
#             if self.size == 1:
#                 self.head = None
#                 self.tail = None
#
#             else:
#                 self.head = self.head.next
#             self.size -= 1
#             return cur.data
#
#         while cur.next:
#             bef = cur
#             cur = cur.next
#
#             if target == cur.data: # 삭제하려는 노드가 첫번째 노드가 아닐때
#                 if cur == self.tail:
#                     self.tail = bef
#
#                 bef.next = cur.next
#                 self.size -= 1
#                 return cur.data
#         return None


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(4)
    linked_list.append(5)
    linked_list.append(2)

    linked_list.reverse()
    linked_list.print_list()
    print(linked_list.tail.data)
    #
    # linked_list.print_list()
    # linked_list.reversed()
    # linked_list.print_list()
