class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node


    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1
    
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def find_middle(self):
        if not self.head:
            return None 

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data  # Slow is now pointing to the middle node
    
    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True 
        return False 
    
    def remove_duplicates(self):
        if not self.head:
            return

        seen = set()  # To store seen values
        current = self.head
        seen.add(current.data)  # Add the first element to the set

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next  # Remove the duplicate
            else:
                seen.add(current.next.data)  # Add new data to the set
                current = current.next  # Move to the next node

    def merge_sorted(list1, list2):
        # Dummy node to serve as the starting point for the merged list
        dummy = Node(0)
        tail = dummy

        current1 = list1.head
        current2 = list2.head

        # Traverse both lists, choosing the smaller current node each time
        while current1 and current2:
            if current1.data < current2.data:
                tail.next = current1
                current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            tail = tail.next

        # Append remaining nodes from either list, if any
        if current1:
            tail.next = current1
        elif current2:
            tail.next = current2

        # Create a new LinkedList to hold the merged list
        merged_list = LinkedList()
        merged_list.head = dummy.next  # The merged list starts after the dummy node
        return merged_list

# Test the append method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

# Test the display method
ll.display()  # Output: 1 -> 2 -> 3

# Test the insert method
ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3

# Test the delete method
ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3

# Test the search method
print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1

# Test the reverse method
ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1

# test to find middle method
print(ll.find_middle())

# test for cycle
print(ll.detect_cycle())

# Testing the remove_duplicates method
ll.remove_duplicates()
ll.display()

# Testing the merge_sorted method
list1 = LinkedList()
list2 = LinkedList()

# Adding elements to the first sorted list
list1.append(1)
list1.append(3)
list1.append(5)

# Adding elements to the second sorted list
list2.append(2)
list2.append(4)
list2.append(6)

# Merging the two sorted lists
merged_list = LinkedList.merge_sorted(list1, list2)

print("Merged Sorted List:")
merged_list.display() 