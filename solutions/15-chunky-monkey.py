import unittest

"""
Chunky Monkey

Write a function that splits a list (first argument) into groups the length of 
size (second argument) and returns them as a two-dimensional list.

"""

def chunk_list_in_groups(lst, size):
    result = []
    index = 0
    while index < len(lst):
        result.append(lst[index:index + size])
        index += size
    return result

print(chunk_list_in_groups(["a", "b", "c", "d"], 2))


"""
Do not change anything below:
"""

class TestChunk(unittest.TestCase):

    def test_chunk1(self):
        self.assertListEqual(chunk_list_in_groups(["a", "b", "c", "d"], 2), [["a", "b"], ["c", "d"]])

    def test_chunk2(self):
        self.assertListEqual(chunk_list_in_groups([0, 1, 2, 3, 4, 5], 3), [[0, 1, 2], [3, 4, 5]])

    def test_chunk3(self):
        self.assertListEqual(chunk_list_in_groups([0, 1, 2, 3, 4, 5], 2), [[0, 1], [2, 3], [4, 5]])

    def test_chunk4(self):
        self.assertListEqual(chunk_list_in_groups([0, 1, 2, 3, 4, 5], 4), [[0, 1, 2, 3], [4, 5]])

    def test_chunk5(self):
        self.assertListEqual(chunk_list_in_groups([0, 1, 2, 3, 4, 5, 6], 3), [[0, 1, 2], [3, 4, 5], [6]])

    def test_chunk6(self):
        self.assertListEqual(chunk_list_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4), [[0, 1, 2, 3], [4, 5, 6, 7], [8]])

    def test_chunk7(self):
        self.assertListEqual(chunk_list_in_groups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2), [[0, 1], [2, 3], [4, 5], [6, 7], [8]])


if __name__ == "__main__":
    unittest.main()