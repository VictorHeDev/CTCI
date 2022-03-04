import time

'''
An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of that type). THey cannot select which specific animal they would like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.
'''

'''
APPROACH
- using a single queue to keep the dogs and cats can be kind of messy -> requires iteration when we have to find the first dog or first cat
- one clean and more efficient way to handle this is to implement 2 stacks: one for dogs and one for cats, and have them in a wrapper class called AnimalQueue
- use timestamps to keep track of when an animal is added to their own prospective stack
'''


class Node:
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

    def __str__(self) -> str:
        return str(self.data)


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def insert(self, node):
        if self.head is None:
            self.head = node
            return self.head
        current_node = self.head
        while current_node.next_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = node

    def pop_head(self):
        if self.head is not None:
            head_to_pop = self.head
            head.self = self.head.next_node
            return head_to_pop
        return None

    def size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            current_node = current_node.next_node
            size += 1
        return size


# Animal Definitions - it is important for Cat and Dog to inherit from Animal because dequeue_any() needs to be able to support returning both the Cat and Dog objects
class Animal:
    def __init__(self, name) -> None:
        self.name = name
        self.time_admitted = time.time()


class Cat(Animal):
    pass


class Dog(Animal):
    pass


class AnimalShelter(LinkedList):
    def enqueue(self, animal):
        animal_node = Node(animal)
        self.insert(animal_node)

    def dequeue_any(self):
        return super().pop_head()

    def dequeue_cat(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Cat):
                prev_node.next_node = current_node.next_node
                return current_node.data
            prev_node = current_node
            current_node = current_node.next_node
        return None

    def dequeue_dog(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            if isinstance(current_node.data, Dog):
                prev_node.next_node = current_node.next_node
                return current_node.data
            prev_node = current_node
            current_node = current_node.next_node
        return None
