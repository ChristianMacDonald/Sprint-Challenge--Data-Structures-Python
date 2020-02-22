import time
import sys

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
# #             duplicates.append(name_1)

# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.instances = 1
#         self.left = None
#         self.right = None
    
#     def insert(self, value):
#         current_node = self
#         hashed_value = hash(value)
#         current_node_hashed_value = hash(current_node.value)
#         if hashed_value < current_node_hashed_value:
#             if current_node.left:
#                 current_node.left.insert(value)
#             else:
#                 current_node.left = BinarySearchTree(value)
#         elif hashed_value > current_node_hashed_value:
#             if current_node.right:
#                 current_node.right.insert(value)
#             else:
#                 current_node.right = BinarySearchTree(value)
#         else:
#             current_node.instances += 1

# def find_duplicates(tree):
#     if tree:
#         if tree.instances > 1:
#             return [tree.value] + find_duplicates(tree.left) + find_duplicates(tree.right)
#         else:
#             return find_duplicates(tree.left) + find_duplicates(tree.right)
#     else:
#         return []

# tree = BinarySearchTree("")
# names_t = names_1 + names_2
# for name in names_t:
#     tree.insert(name)
# duplicates = find_duplicates(tree)

# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

dictionary = {}
names_t = names_1 + names_2
for name in names_t:
    if name in dictionary:
        dictionary[name] += 1
    else:
        dictionary[name] = 1

duplicates = [name for name in dictionary if dictionary[name] > 1]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")