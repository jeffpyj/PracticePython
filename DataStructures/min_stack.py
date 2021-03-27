""" use list to implement minstack
.append()
.pop()
"""


class MinStack:

    def __init__(self):
        self._list = []

    def push(self, value):
        min_value = value if len(self._list) == 0 else min(
            self._list[-1][1], value)
        self._list.append((value, min_value))

    def pop(self):
        return self._list.pop()

    def top(self):
        return self._list[-1]


if __name__ == '__main__':

    input_list = [5, 2, 6, 7, 1]
    minS = MinStack()
    for i in input_list:
        minS.push(i)

    print("min value in this stack right now is", minS.top()[1])
    minS.pop()
    print("min value in this stack right now is", minS.top()[1])
