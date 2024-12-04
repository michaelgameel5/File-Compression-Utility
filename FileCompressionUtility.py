import collections
import os
import heapq

class Node:
    def __init__(self, char=None, freq=0):
        self.char = char  # Character
        self.freq = freq  # Frequency
        self.left = None  # Left child
        self.right = None  # Right child

    # Define less-than for priority queue (heap)
    def __lt__(self, other):
        return self.freq < other.freq

        
class FileCompressionUtility:
    def __init__(self):
        self.frequency_table = {}
        self.huffman_tree = None
        self.huffman_codes = {}
    
    # Frequency table generation
    def build_frequency_table(self, file_path):
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return None

        try:
            with open(file_path, "r") as file:
                self.frequency_table = collections.Counter(file.read())
        except IOError as e:
            print(f"An error occurred while opening the file: {e}")

    # Build the Huffman Tree
    def build_huffman_tree(self):
        if not self.frequency_table:
            print("Error: Frequency table is empty. Build the frequency table first.")
            return

        # Create a priority queue with nodes
        heap = [Node(char, freq) for char, freq in self.frequency_table.items()]
        heapq.heapify(heap)

        # Build the tree by combining two smallest nodes iteratively
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = Node(None, left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)

        # The last node is the root of the tree
        self.huffman_tree = heap[0] if heap else None

    # Generate Huffman codes using the tree
    def generate_huffman_codes(self, node=None, current_code=""):
        if node is None:
            node = self.huffman_tree

        if node is None:
            print("Error: Huffman tree is empty. Build the tree before generating codes.")
            return

        # Leaf node: add to codes dictionary
        if node.char is not None:
            self.huffman_codes[node.char] = current_code
            return

        # Traverse left and right
        if node.left:
            self.generate_huffman_codes(node.left, current_code + "0")
        if node.right:
            self.generate_huffman_codes(node.right, current_code + "1")
 

    # File compression
    def compress_file(self, file_path, output_path):
        pass

    # Save metadata                                             
    def save_metadata(self, output_path) :
        pass

    # Load metadata
    def load_metadata(self, file_path):
        pass

    # Huffman tree reconstruction
    def reconstruct_huffman_tree(self) :
        pass

    # File decompression
    def decompress_file(self, compressed_path, output_path):
        pass

f = FileCompressionUtility()
f.build_frequency_table("file.txt")
f.build_huffman_tree()
f.generate_huffman_codes()