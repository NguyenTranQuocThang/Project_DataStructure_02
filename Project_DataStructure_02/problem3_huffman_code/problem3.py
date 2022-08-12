# https://cmps-people.ok.ubc.ca/ylucet/DS/Huffman.html
import sys
from queue import PriorityQueue


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
    node = data[2]
    state = State(node)
    state.huffman_code = ""
    stack.push(state)
    while(node):

        #

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
            if(state.get_node().character is not None):
                dic[state.get_node().character] = state.huffman_code
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
    return dic


def huffman_encoding(data):

    queue = PriorityQueue()

    count = 0

    if len(data) == 0:
        return "", None

    if len(data) == 1:
        return '0', (0, 0, TreeNode(data, 1))

    characters = {}

    for i in data:
        characters[i] = characters.get(i, 0) + 1

    for key, value in characters.items():
        queue.put((value, count, key))
        count += 1
    # while not queue.empty():
    #     item = queue.get()
    #     print(item)
    while not queue.empty():
        if(queue.qsize() == 1):
            node = queue.get()
            dic = traverse_node(node)
            for key, value in dic.items():
                data = data.replace(key, value)
            return data, node

        first = queue.get()

        node_first = first[2]
        if(not isinstance(node_first, TreeNode)):
            node_first = TreeNode(first[2], first[0])

        second = queue.get()
        node_second = second[2]
        if(not isinstance(node_second, TreeNode)):
            node_second = TreeNode(second[2], second[0])
        node_internal = TreeNode(
            None, node_first.frequence + node_second.frequence)

        node_internal.left = node_first

        node_internal.right = node_second

        queue.put((node_internal.frequence, count, node_internal))
        count += 1


def huffman_decoding(data, node):
    if len(data) == 0 or node == None:
        return ""
    decode_data = ''
    root = node[2]

    # check case 1 character
    if root.character is not None:
        return root.character

    for i in data:
        if i == '0':
            root = root.get_left_child()
        else:
            root = root.get_right_child()
        if root.character is not None:
            decode_data += root.character
            root = node[2]
    return decode_data

    # for key, value in reversed(dic).items():
    #     data = data.replace(value, key)
    # return data


# if _name_ == "_main_":
#     codes = {}
a_great_sentence = "The bird is the word"
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = huffman_encoding(a_great_sentence)
print("The size of the encoded data is: {}\n".format(
    sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, tree)
print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
a_great_sentence = "Fpt software Fpt software Fpt software Fpt software Fpt software Fpt software Fpt software Fpt software Fpt software Fpt software"
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print("The content of the data is: {}\n".format(a_great_sentence))
encoded_data, tree = huffman_encoding(a_great_sentence)
print("The size of the encoded data is: {}\n".format(
    sys.getsizeof(int(encoded_data, base=2))))
print("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data = huffman_decoding(encoded_data, tree)
print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print("The content of the encoded data is: {}\n".format(decoded_data))
# Test Case 2
a_great_sentence = "a"
encoded_data, tree = huffman_encoding(a_great_sentence)
decoded_data = huffman_decoding(encoded_data, tree)
print(a_great_sentence == decoded_data)
# Test Case 3
a_great_sentence = ""
encoded_data, tree = huffman_encoding(a_great_sentence)
decoded_data = huffman_decoding(encoded_data, tree)
print(a_great_sentence == decoded_data)
