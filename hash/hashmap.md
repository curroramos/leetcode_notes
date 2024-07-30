### Hash Sets and Hash Maps Overview

Hash sets and hash maps are data structures that provide efficient insertion, deletion, and search operations. They use hash functions to compute an index (or hash code) into an array of buckets or slots, from which the desired value can be found.

### Hash Set

A hash set is a collection of unique elements. It is implemented using a hash table, where each element is stored at a position determined by a hash function.

#### Operations

1. **Insertion:** Add an element to the set.
2. **Deletion:** Remove an element from the set.
3. **Search:** Check if an element is in the set.
4. **Traversal:** Iterate over all elements in the set.

**Example Code for Hash Set:**
```python
class HashSet:
    def __init__(self):
        self.bucket = [[] for _ in range(10)]

    def _hash(self, key):
        return key % len(self.bucket)

    def add(self, key):
        hash_key = self._hash(key)
        if key not in self.bucket[hash_key]:
            self.bucket[hash_key].append(key)

    def remove(self, key):
        hash_key = self._hash(key)
        if key in self.bucket[hash_key]:
            self.bucket[hash_key].remove(key)

    def contains(self, key):
        hash_key = self._hash(key)
        return key in self.bucket[hash_key]

# Example usage
hash_set = HashSet()
hash_set.add(10)
hash_set.add(20)
hash_set.add(15)
print(hash_set.contains(10))  # Output: True
print(hash_set.contains(25))  # Output: False
hash_set.remove(10)
print(hash_set.contains(10))  # Output: False
```

### Hash Map

A hash map (or dictionary) is a collection of key-value pairs. It is implemented using a hash table, where each key-value pair is stored at a position determined by a hash function applied to the key.

#### Operations

1. **Insertion:** Add a key-value pair to the map.
2. **Deletion:** Remove a key-value pair from the map.
3. **Search:** Retrieve the value associated with a given key.
4. **Traversal:** Iterate over all key-value pairs in the map.

**Example Code for Hash Map:**
```python
class HashMap:
    def __init__(self):
        self.bucket = [[] for _ in range(10)]

    def _hash(self, key):
        return hash(key) % len(self.bucket)

    def put(self, key, value):
        hash_key = self._hash(key)
        found = False
        for i, kv in enumerate(self.bucket[hash_key]):
            if kv[0] == key:
                self.bucket[hash_key][i] = (key, value)
                found = True
                break
        if not found:
            self.bucket[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        for kv in self.bucket[hash_key]:
            if kv[0] == key:
                return kv[1]
        return None

    def remove(self, key):
        hash_key = self._hash(key)
        for i, kv in enumerate(self.bucket[hash_key]):
            if kv[0] == key:
                del self.bucket[hash_key][i]
                break

# Example usage
hash_map = HashMap()
hash_map.put("apple", 10)
hash_map.put("banana", 20)
hash_map.put("orange", 15)
print(hash_map.get("apple"))  # Output: 10
print(hash_map.get("grape"))  # Output: None
hash_map.remove("apple")
print(hash_map.get("apple"))  # Output: None
```

### Hash Functions

A hash function is a function that takes an input (or 'key') and returns a fixed-size string of bytes. The output is typically a 'hash code' used to index an array of buckets or slots.

#### Properties of a Good Hash Function

1. **Deterministic:** Same input should always produce the same hash.
2. **Efficiently Computable:** The hash function should be easy to compute.
3. **Uniform Distribution:** The hash function should distribute keys uniformly across the buckets.
4. **Minimize Collisions:** The hash function should minimize the number of collisions, where two keys hash to the same bucket.

### Handling Collisions

1. **Chaining:** Use a list to store multiple elements that hash to the same bucket.
2. **Open Addressing:** Find another slot within the array using a probing sequence (e.g., linear probing, quadratic probing, double hashing).

#### Example of Chaining
```python
class HashMapWithChaining:
    def __init__(self):
        self.bucket = [[] for _ in range(10)]

    def _hash(self, key):
        return hash(key) % len(self.bucket)

    def put(self, key, value):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.bucket[hash_key]):
            if k == key:
                self.bucket[hash_key][i] = (key, value)
                return
        self.bucket[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        for k, v in self.bucket[hash_key]:
            if k == key:
                return v
        return None

    def remove(self, key):
        hash_key = self._hash(key)
        for i, (k, v) in enumerate(self.bucket[hash_key]):
            if k == key:
                del self.bucket[hash_key][i]
                return

# Example usage
hash_map_chaining = HashMapWithChaining()
hash_map_chaining.put("apple", 10)
hash_map_chaining.put("banana", 20)
hash_map_chaining.put("orange", 15)
print(hash_map_chaining.get("apple"))  # Output: 10
print(hash_map_chaining.get("grape"))  # Output: None
hash_map_chaining.remove("apple")
print(hash_map_chaining.get("apple"))  # Output: None
```

#### Example of Open Addressing
```python
class HashMapWithOpenAddressing:
    def __init__(self):
        self.size = 10
        self.bucket = [None] * self.size
        self.load_factor = 0.7
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def _rehash(self):
        old_bucket = self.bucket
        self.size *= 2
        self.bucket = [None] * self.size
        self.count = 0
        for item in old_bucket:
            if item is not None:
                self.put(item[0], item[1])

    def put(self, key, value):
        if self.count / self.size >= self.load_factor:
            self._rehash()
        hash_key = self._hash(key)
        while self.bucket[hash_key] is not None:
            if self.bucket[hash_key][0] == key:
                self.bucket[hash_key] = (key, value)
                return
            hash_key = (hash_key + 1) % self.size
        self.bucket[hash_key] = (key, value)
        self.count += 1

    def get(self, key):
        hash_key = self._hash(key)
        while self.bucket[hash_key] is not None:
            if self.bucket[hash_key][0] == key:
                return self.bucket[hash_key][1]
            hash_key = (hash_key + 1) % self.size
        return None

    def remove(self, key):
        hash_key = self._hash(key)
        while self.bucket[hash_key] is not None:
            if self.bucket[hash_key][0] == key:
                self.bucket[hash_key] = None
                self.count -= 1
                return
            hash_key = (hash_key + 1) % self.size

# Example usage
hash_map_open = HashMapWithOpenAddressing()
hash_map_open.put("apple", 10)
hash_map_open.put("banana", 20)
hash_map_open.put("orange", 15)
print(hash_map_open.get("apple"))  # Output: 10
print(hash_map_open.get("grape"))  # Output: None
hash_map_open.remove("apple")
print(hash_map_open.get("apple"))  # Output: None
```

### Applications of Hash Sets and Hash Maps
1. **Databases:** Efficiently indexing and retrieving data.
2. **Caching:** Storing frequently accessed data for fast retrieval.
3. **Symbol Tables:** Storing variables and their values in interpreters and compilers.
4. **Counting Frequency:** Counting occurrences of elements in data processing.

### Advantages and Disadvantages

**Advantages:**
- **Fast Operations:** Average-case time complexity of O(1) for insertion, deletion, and search.
- **Simple Implementation:** Easy to implement and understand.

**Disadvantages:**
- **Hash Collisions:** Requires handling collisions which can degrade performance.
- **Memory Usage:** Can use more memory compared to other data structures.
- **Dependent on Hash Function:** Performance and correctness depend heavily on the quality of the hash function.
