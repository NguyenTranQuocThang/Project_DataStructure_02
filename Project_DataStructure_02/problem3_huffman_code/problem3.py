# https://cmps-people.ok.ubc.ca/ylucet/DS/Huffman.html
from inspect import stack
from platform import node
import sys
from queue import PriorityQueue, Queue


class Stack():
    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    def is_empty(self):
        return len(self.list) == 0


class State(object):
    def __init__(self, node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        self.huffman_code = None

    def get_node(self):
        return self.node

    def get_visited_left(self):
        return self.visited_left

    def get_visited_right(self):
        return self.visited_right

    def set_visited_left(self):
        self.visited_left = True

    def set_visited_right(self):
        self.visited_right = True


class TreeNode:
    def __init__(self, character, frequence):
        self.left = None
        self.right = None
        self.character = character
        self.frequence = frequence
     # set a node for the left child

    def set_left_child(self, left):
        self.left = left

    # set a node for the right child
    def set_right_child(self, right):
        self.right = right

    # get the node of left child
    def get_left_child(self):
        return self.left

    # get the node of right child
    def get_right_child(self):
        return self.right

    # check if node has left child -> return boolean
    def has_left_child(self):
        return self.left != None

    # check if node has right child -> return boolean
    def has_right_child(self):
        return self.right != None


def traverse_node(data):
    dic = {}
    stack = Stack()
    node = data[1]
    state = State(node)
    state.huffman_code = ""
    stack.push(state)
    while(node):
        if node.has_left_child() and not state.get_visited_left():
            huff_code_father = state.huffman_code
            state.set_visited_left()
            node = node.get_left_child()
            state = State(node)
            state.huffman_code = huff_code_father + '0'
            stack.push(state)
        elif node.has_right_child() and not state.get_visited_right():
            huff_code_father = state.huffman_code
            state.set_visited_right()
            node = node.get_right_child()
            state = State(node)
            state.huffman_code = huff_code_father + '1'
            stack.push(state)
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None


def huffman_encoding(data):
    if len(data) == 0:
        return "", None

    characters = {}

    for i in data:
        characters[i] = characters.get(i, 0) + 1
    queue = PriorityQueue()

    for key, value in characters.items():
        queue.put((value, key))
    # while not queue.empty():
    #     item = queue.get()
    #     print(item)
    while not queue.empty():
        if(queue.qsize() == 1):
            traverse_node(queue.get())
            return

        first = queue.get()

        node_first = TreeNode(first[1], first[0])

        second = queue.get()

        node_second = TreeNode(second[1], second[0])

        node_internal = TreeNode(
            None, node_first.frequence + node_second.frequence)

        node_internal.left = node_first

        node_internal.right = node_second

        queue.put((node_internal.frequence, node_internal))

# def huffman_decoding(data, tree):
#     pass


# if _name_ == "_main_":
#     codes = {}
#     a_great_sentence = "The bird is the word"
#     print("The size of the data is: {}\n".format(
#         sys.getsizeof(a_great_sentence)))
#     print("The content of the data is: {}\n".format(a_great_sentence))
#     encoded_data, tree = huffman_encoding(a_great_sentence)
#     print("The size of the encoded data is: {}\n".format(
#         sys.getsizeof(int(encoded_data, base=2))))
#     print("The content of the encoded data is: {}\n".format(encoded_data))
#     decoded_data = huffman_decoding(encoded_data, tree)
#     print("The size of the decoded data is: {}\n".format(
#         sys.getsizeof(decoded_data)))
#     print("The content of the encoded data is: {}\n".format(decoded_data))
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
huffman_encoding('fpt')


# Test Case 1

# Test Case 2

# Test Case 3
