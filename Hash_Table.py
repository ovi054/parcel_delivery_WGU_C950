# Daryl Augustin 
# creating has table here
class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        #appends whatever I put into key and item into the self.map list

class HashMap:
#hashing maps a location to an array
# so that it doesnt run the list  at once but instead does it in chunks of 10
    def __init__(self, cap=10):
        # Creates a list that runs the length of 10
        self.map = []
        for i in range(cap):
            self.map.append([])
         #.append() takes an object as an argument and adds it to the end of an existing list, right after its last element:
    # private getter to create a hash key
    # now we make our hash key O(1) or O(N)
    def get_hashkey(self, key):
        bucket = int(key) % len(self.map)
        return bucket

    # Push the package into the hash table time complexity O(N)
    def insert(self, key, value):
        key_hash = self.get_hashkey(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[key_hash].append(key_value)
            return True

    # Update package in hash table -> O(n)
    def update(self, key, value):
        key_hash = self.get_hashkey(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    print(pair[1])
                    return True
        else:
            print('Error with updating on key: ' + key)

    # Grab a value from the hash table
    # Space-time complexity is O(N)
    def get_value(self, key):
        key_hash = self.get_hashkey(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    # take out the value from the hash table now and STC is O(N)
    def delete(self, key):
        key_hash = self.get_hashkey(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False
