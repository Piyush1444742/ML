
# Huffman Encoding using Greedy Strategy

import heapq

# Create a node
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Generate Huffman Codes
def generate_codes(root, code, codes):

    if root is None:
        return

    # If leaf node, store the code
    if root.char is not None:
        codes[root.char] = code
        return

    generate_codes(root.left, code + "0", codes)
    generate_codes(root.right, code + "1", codes)


# Main Program
chars = ['A', 'B', 'C', 'D', 'E', 'F']
freq = [5, 9, 12, 13, 16, 45]

heap = []

# Insert characters into Min Heap
for i in range(len(chars)):
    node = Node(chars[i], freq[i])
    heapq.heappush(heap, (node.freq, i, node))

# Build Huffman Tree
count = len(chars)

while len(heap) > 1:

    freq1, _, left = heapq.heappop(heap)
    freq2, _, right = heapq.heappop(heap)

    new_node = Node(None, freq1 + freq2)

    new_node.left = left
    new_node.right = right

    heapq.heappush(heap, (new_node.freq, count, new_node))
    count += 1

# Generate Huffman Codes
root = heapq.heappop(heap)[2]

codes = {}
generate_codes(root, "", codes)

# Display codes
print("Huffman Codes:")

for char in chars:
    print(char, ":", codes[char])
