class RandomizedSet:

    def __init__(self):
        self.num_list = []
        self.num_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.num_list)
        self.num_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        # Move the last element to the place idx of the element to delete
        last_element = self.num_list[-1]
        idx_to_remove = self.num_to_index[val]
        self.num_list[idx_to_remove] = last_element
        self.num_to_index[last_element] = idx_to_remove
        # Remove last element
        self.num_list.pop()
        del self.num_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.num_list)
