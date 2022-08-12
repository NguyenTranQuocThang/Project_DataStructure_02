import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode(
            'utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values


# Test Case 1

block1 = Block('2022-12-08 17:49:00', 'information-block1', 0)
# Test Case 2
block2 = Block('2022-12-08 17:49:00', 'information-block2', block1.hash)
# Test Case 3
block3 = Block('2022-12-08 17:49:00', 'information-block3', block2.hash)

print(block1.previous_hash)
print(block1.hash)

print(block2.previous_hash)
print(block2.hash)

print(block3.previous_hash)
print(block3.hash)
