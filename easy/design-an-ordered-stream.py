## constraints:
## 1 <= n <= 1000
## 1 <= id <= n
## Each call to insert will have a unique id
## Exactly n calls will be made to insert


## Time complexity: O(N)
## Space complexity: O(N)

class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 0
        self.stream = [None] * n


    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value

        if self.ptr < idKey:
            return []
        else:
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[idKey:self.ptr]
