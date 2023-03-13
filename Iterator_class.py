# TASK 1

class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list
        self.len_main_list = len(self.main_list)
        self.main_list_cursor = -1

    def __iter__(self):
        self.main_list_cursor += 1
        self.nested_list_cursor = 0

        return self

    def __next__(self):

        if self.nested_list_cursor == len(self.main_list[self.main_list_cursor]):
            iter(self)
        if self.main_list_cursor == self.len_main_list:
            raise StopIteration
        self.nested_list_cursor += 1

        return self.main_list[self.main_list_cursor][self.nested_list_cursor - 1]


# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]

# for item in FlatIterator(list_of_lists_1):
#     print(item)