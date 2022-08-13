import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode(
            'utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def __repr__(self):
        s = "Timestamp: " + self.timestamp.strftime("%m/%d/%Y, %H:%M:%S")
        s += "\nData: "+self.data
        s += "\nSHA256 Hash: "+self.hash
        if self.previous_hash is not None:
            s += "\nPrivious Hash: "+self.previous_hash
        else:
            s += "\nPrivious Hash: None"
        return s


class Blockchain:
    def __init__(self, timestamp, data):
        root_block = Block(timestamp, data)
        self.current_block = root_block

    def add_block(self, block):
        block.previous_hash = self.current_block.hash
        self.current_block = block

    def get_current_block(self):
        return self.current_block

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

print("--------------------------------------------------------")
print("#Block root: ")
block_chain = Blockchain(datetime.now(), "information of root block data")
print(block_chain.get_current_block())

# Test Case 1
block1 = Block(datetime.now(), 'information-block1')
block_chain.add_block(block1)
print("--------------------------------------------------------")
print("#Block 1: ")
print(block_chain.get_current_block())
# Test Case 2
block2 = Block(datetime.now(), 'information-block2')
block_chain.add_block(block2)
print("--------------------------------------------------------")
print("#Block 2: ")
print(block_chain.get_current_block())
# Test Case 3
block3 = Block(datetime.now(), 'information-block3')
block_chain.add_block(block3)
print("--------------------------------------------------------")
print("#Block 3: ")
print(block_chain.get_current_block())
