class ArrayClass:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity

    def __len__(self):
        return self.size

    def append(self, value):
        if self.size == self.capacity:
            self._resize()
        self.data[self.size] = value
        self.size += 1

    def _resize(self):
        print("Resizing...")
        self.capacity *= 2
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of bounds")

    def set(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def __str__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self._resize()
        # Shift elements to right
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = value
        self.size += 1

    def remove(self, value):
        found = False
        for i in range(self.size):
            if self.data[i] == value:
                found = True
                # Shift left all the elements after i
                for j in range(i, self.size - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.size - 1] = None
                self.size -= 1
                break
        if not found:
            raise ValueError("Value not found in array")

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of bounds")

    def __setitem__(self, index, value):
        if 0 <= index < self.size:
            self.data[index] = value
        else:
            raise IndexError("Index out of bounds")

    def partition(self, arr, low, high):
        # selecting pivot point as last element
        pivot = arr[high]
        # selecting "i" pointer as "lower bound" - 1
        i = low - 1
        # selection "j" as "lower bound"
        j = low

        # condition to iterate is "j" should be less than "upper bound - (high)", :. We want to iterate till pivot exculding pivot
        while j < high:
            # if j's value is less than pivot, else do nothing keep it there only
            if arr[j] < pivot:
                # increment i by 1
                i += 1
                # swap "i" and "j"'s value
                arr[i], arr[j] = arr[j], arr[i]
            # our, "manjhi" variable "j" should be incremented by 1 everytime irrespective of any condition
            j += 1
        # when the j index is equal to pivot index - 1, then we swap values of our pivot and ("i" + 1) element
        arr[high], arr[i + 1] = arr[i + 1], arr[high]
        # we return i + 1 because its the new pivot
        return i + 1

    # Array Sorting Methods :
    def quicksort(self, arr, low, high):
        # Pseudo Code
        # 1. Pick a pivot point "p" (usually the last or random)
        # 2. start a pointer at the first element "i"
        # 3. start a pointer at the second last element "j"
        # 4. "i" should look for elements that are greater than "p"
        # 5. "j" should look for elements that are less than "p"
        # 6. while finding elements if "j" index <= "i" index, then swap elements of "i" and "p"
        # 7. keep calling this is recursion for subarrays

        # condition to check if the input arr pointers have at least 1 element
        if low < high:
            pivot = self.partition(arr, low, high)
            self.quicksort(arr, low, pivot - 1)
            self.quicksort(arr, pivot + 1, high)


def __init__():
    arr = ArrayClass()
    arr.append(6)
    arr.append(3)
    arr.append(8)
    arr.append(4)
    arr.append(7)
    print("Before sorting:", arr)
    arr.quicksort(arr, 0, arr.size - 1)
    print("After sorting :", arr)


__init__()
