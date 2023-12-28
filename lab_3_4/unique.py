from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get("ignore_case", False)
        self.items = iter(items)
        self.returned_items = set()

    def __next__(self):
        found = False
        while not found:
            item = next(self.items)

            if self.ignore_case and isinstance(item, str):
                if item.lower() not in self.returned_items:
                    self.returned_items.add(item.lower())
                    return item
            else:
                if item not in self.returned_items:
                    self.returned_items.add(item)
                    return item
        raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))  # [1, 2]

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    print(list(Unique(data)))  # ['a', 'A', 'b', 'B']

    data = gen_random(10, 1, 3)
    print(list(Unique(data)))  # [2, 1, 3]

    data = ["a", "A", "b", "B", "a", "A", "b", "B"]
    print(list(Unique(data, ignore_case=True)))  # ['a', 'b']
