# Dictionary operations
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Original Dictionary:", Dict)

# 1. Accessing values using keys
print("Value for key 2:", Dict[2])

# 2. Adding a new key-value pair
Dict[4] = 'Programming'
print("After adding a new key-value pair:", Dict)

# 3. Removing a key-value pair using pop
removed_value = Dict.pop(3)
print(f"After removing key 3 (value: {removed_value}):", Dict)

# 4. Getting all keys
keys = Dict.keys()
print("All keys:", list(keys))

# 5. Checking if a key exists
print("Is key 1 present?", 1 in Dict)


print("\n---\n")


# Tuple operations
thistuple = ("apple", "banana", "cherry")
print("Original Tuple:", thistuple)

# 1. Accessing an element by index
print("Element at index 1:", thistuple[1])

# 2. Counting occurrences of an element
count_apple = thistuple.count("apple")
print("Count of 'apple':", count_apple)

# 3. Getting the index of an element
index_cherry = thistuple.index("cherry")
print("Index of 'cherry':", index_cherry)

# 4. Concatenating two tuples
new_tuple = thistuple + ("date", "elderberry")
print("After concatenating with another tuple:", new_tuple)

# 5. Slicing the tuple
sliced_tuple = thistuple[1:]
print("Sliced tuple from index 1:", sliced_tuple)
