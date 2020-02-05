from stack import Stack

# Implemented with Python lists, kinda defeats the purpose but oh well
# Also implemented with chaining, using stacks 
class HashTable:
    def __init__(self, bucketSize = 1000):
        self.bucketSize = bucketSize
        self.bucket = []
        for index in range(self.bucketSize):
            self.bucket.append(Stack())

    # Hashing function
    def hashKey(self, key):
        return key % self.bucketSize

    # Pushes to stack at hash ID
    def insert(self, key, value):
        hashId = self.hashKey(key)
        self.bucket[hashId].push(value)
        return hashId

    # Pops from stack at hash ID
    def remove(self, key):
        hashId = self.hashKey(key)
        ret = self.bucket[hashId].pop()
        return ret

    # Only peeks top of stack at hash ID
    def search(self, key):
        hashId = self.hashKey(key)
        ret = self.bucket[hashId].peek()
        return ret
