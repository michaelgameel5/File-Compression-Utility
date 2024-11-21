import collections
import os
import heapq

class FileCompressionUtility:
    def __init__(self):
        self.frequency_table = collections.Counter()
        self.huffman_tree = None
        self.huffman_codes = {}
    
    # Frequency table generation
    def build_frequency_table(self, file_path):
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return
        
        try:
            with open(file_path, "r") as file:
                self.frequency_table = collections.Counter(file.read())
        except IOError as e:
            print(f"An error occurred while opening the file: {e}")

    # Huffman tree construction
    def build_huffman_tree(self):
        heap = [[weight,[char,""]]for char ,weight in self.frequency_table.items()]
        heapq.heapify(heap)
        while len(heap) >1:
            ln = heapq.heappop(heap)
            rn = heapq.heappop(heap)
            for pair in ln[1:]:
                pair[1]+= '0'
            for pair in rn[1:]:
                pair[1]+= '1'
            heapq.heappush(heap,[ln[0]+rn[0]] + ln[1:] + rn[1:])

        self.huffman_tree = sorted(heapq.heappop(heap)[ 1:] , key = lambda p : ( len( p[-1] ) , p))
    # Huffman code generation
    def generate_huffman_codes(self):
        pass

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