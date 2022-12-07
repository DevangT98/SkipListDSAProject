from OrderedDictionary import *
import random

from collections import OrderedDict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.above = None
        self.below = None
        self.next = None
        self.prev = None


class SkipList(OrderedDictionary):

    skip_list = OrderedDictionary()

    negative_inf = float('-inf')
    positive_inf = float('inf')

    height = 0
    count = 0

    def __init__(self):
        self.head = Node(SkipList.negative_inf, None)
        self.tail = Node(SkipList.positive_inf, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertElement(self, k, v):
        p = self.findElement(k)
        # print(p.key, p.value)
        level = -1
        if p.key == k:
            old_val = p.value
            p.value = v

            return old_val

        self.count += 1
        while True:
            res = bool(random.getrandbits(1))
            level += 1
            # self.count += 1
            self.increase_level(level)
            q = p
            while p.above is None:
                p = p.prev
                # print(f"TYPE OF P after while inside insertElement {type(p)}")
            p = p.above
            # print(f"value and type of p after p=p.above  {p.key}, {p.value},{type(p)}")
            q = self.insert_after_above(p, q, k, v)
            # print(f"q after insert above values: {q.key},{q.value}")
            if not res:
                break

        return None

    def insert_after_above(self, p, q, k, v):
        new_node = Node(k, v)
       # print(f"New node inside insert after above method key = {new_node.key}, value = {new_node.value}, VALUE OF P = {p}")
        node_before_new_node = p.below.below

        # print(f"Node before new node value inside insert after above: {node_before_new_node}\n")

        self.set_before_and_after_references(q, new_node)
        self.set_above_and_below_references(
            p, k, new_node, node_before_new_node)

        return new_node

    def set_before_and_after_references(self, q, new_node) -> None:
        new_node.next = q.next
        new_node.prev = q
        q.next.prev = new_node
        q.next = new_node

    def set_above_and_below_references(self, p, k, new_node, node_before_new_node):
        if node_before_new_node is not None:
            while True:
                if node_before_new_node.next.key != k:
                    node_before_new_node = node_before_new_node.next
                else:
                    break
        new_node.below = node_before_new_node.next if node_before_new_node else None
        if node_before_new_node:
            node_before_new_node.next.above = new_node if new_node else None

        if p is not None:
            if p.next.key == k:
                new_node.above = p.next

    def increase_level(self, level):
        if level >= self.height:
            self.height += 1

            self.add_empty_level()

    def add_empty_level(self):
        new_head = Node(SkipList.negative_inf, None)
        new_tail = Node(SkipList.positive_inf, None)

        new_head.next = new_tail
        new_head.below = self.head
        # When we create a new level, there won't be anything that level except -inf and +inf with -inf point to +inf and vice versa
        new_tail.prev = new_head
        new_tail.below = self.tail

        self.head.above = new_head
        self.tail.above = new_tail

        self.head = new_head
        self.tail = new_tail

    def findElement(self, k):
        p = self.head
        while p.below is not None:
            p = p.below
            while p.next.key <= k:
                p = p.next
        return p

    def closestKeyAfter(self, k):
        node = self.findElement(k)
        if node is None or node.next.key == SkipList.positive_inf:
            return None
        else:
            return self.findElement(node.next.key)

    def closestKeyBefore(self, k):
        node = self.findElement(k)
        print(
            f"Closest key before - find element returned: {node.key}, {node.value}")
        if node is None or node.prev.key == SkipList.negative_inf:
            return None
        else:
            return self.findElement(node.prev.key)

    def removeElement(self, k):
        node = self.findElement(k)

        if node.key != k:
            return None

        self.remove_references(node)

        while node is not None:
            self.remove_references(node)

            if node.above is not None:
                node = node.above
            else:
                break
        self.count -= 1
        return node

    def remove_references(self, node):

        node_after_to_be_removed = node.next
        node_before_to_be_removed = node.prev

        node_before_to_be_removed.next = node_after_to_be_removed
        node_after_to_be_removed.prev = node_before_to_be_removed

    def display(self):
        output = ""
        start = self.head
        highest_level = start
        level = self.height
        ordered_dict = OrderedDict()
        while highest_level is not None:
            output += "\n" + f"Level[{str(level)}] :"

            while start is not None:
                output += " " + str(start.key) + " " + str(start.value)
                if start.next is not None:
                    output += " --> "

                start = start.next
            highest_level = highest_level.below
            start = highest_level
            level -= 1
        print(output)

    def size(self):
        print(f"\nThe number of keys in the SkipList are: {self.count}\n")
