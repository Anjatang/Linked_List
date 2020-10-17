# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 21:38:12 2020

@author: anjat
"""

import time
import random
import matplotlib.pyplot as plt

# define the attribute of each element in the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# define the overall structure and functions of the Linked List
class Linked_List:
    def __init__(self):
        self.head =None
    
    def print_List(self):
        current_Node = self.head
        if self.head == None:
            print('List is empty')
        while current_Node != None:
            print(current_Node.data)
            current_Node = current_Node.next
        print('End of List')
    
    # create the Linked List        
    def append(self, new_Node):
        if self.head == None:
            self.head = new_Node
            return
        last_Node = self.head
        while last_Node.next != None:
            last_Node = last_Node.next
        last_Node.next = new_Node

    # insert at the beginning of the Linked List
    def prepend(self, new_Node):
        new_Node.next = self.head
        self.head = new_Node
    
    # insert behind one specific element (head as defined in assignment)
    def insert(self, prev_Node, new_Node):
        if prev_Node == None:
            print('Previous Node not in List')
            return
        new_Node.next = prev_Node.next
        prev_Node.next = new_Node

    # search for a specific element        
    def get(self, data):
        if self.head == None:
            print('List is empty')
        else:
            current_Node = self.head
            current_Position = 0
            while current_Node != None:
                if current_Node.data == data:
                    # print(current_Position, current_Node.data)
                    return current_Node
                else:
                    current_Node = current_Node.next
                    current_Position += 1
            print('data not found in list')
            
        



lengths_to_run = [1000, 2000, 3000, 4000, 8000, 16000, 32000]

time_insert_results = []
for length in lengths_to_run:
    L_List = Linked_List()
    for i in range(length):
        Node_List = Node(i)
        L_List.append(Node_List)

    time_insert = 0
    new_Node = Node(random.randrange(length))
    start = time.time()
    L_List.insert(L_List.head, new_Node)
    end = time.time()
    time_insert = end - start
    time_insert_results.append(time_insert)
    
print(time_insert_results)
    
plt.plot(lengths_to_run, time_insert_results, label = 'Insert', marker = 'x')
plt.xlabel('List Size')
plt.ylabel('Time Complexity')
plt.title('Time Complexity of Inserting to Linked List: O(1)')
plt.legend()
plt.show()
    
    

