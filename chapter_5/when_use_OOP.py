# When will use OOP.
# ------------------------------


import ctypes


class Array:
    _double = 2

    def __init__(self, size):
        self._idx = 0
        self._capticaty = 30
        array_data_type = ctypes.py_object * self._capticaty
        self.size = size
        self.memory = array_data_type()
        for i in range(size):
            self.memory[i] = None

    def _extend_capticaty(self):
        self._capticaty *= Array._double

        array_data_type = ctypes.py_object * self._capticaty
        new_memory = array_data_type()

        for i in range(self.size):
            new_memory[i] = self.memory[i]

        self.memory = new_memory

    def append(self, value):
        if self.size == self._capticaty:
            self._extend_capticaty()
        self.memory[self.size] = value
        self.size += 1

    def insert(self, idx, value):
        assert 0 <= idx <= self.size

        if self.size == self._capticaty:
            self._extend_capticaty()

        for i in range(self.size - 1, idx - 1, -1):
            self.memory[i + 1] = self.memory[i]

        self.memory[idx] = value
        self.size += 1

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        return self.memory[idx]

    def __setitem__(self, idx, value):
        self.memory[idx] = value

    def __iter__(self):
        self._idx = 0
        return self

    def __next__(self):
        if self._idx >= self.size:
            raise StopIteration

        value = self.memory[self._idx]
        self._idx += 1
        return value


def main():
    array = Array(6)

    for i in range(6):
        array[i] = i + 1

    array.insert(0, 55)
    array.append(992)
    array.append(992)
    array.append(992)
    
    for i in array:
        print(i)


if __name__ == "__main__":
    main()
