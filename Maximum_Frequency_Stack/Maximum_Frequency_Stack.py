"""
Stack that pops the most frequently pushed element first
"""
from collections import deque

class FreqStack:
    """
    Frequency-based stack — pop returns the most frequent element
    """
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        """
        Push a value and update its frequency and group
        """
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        current_freq = self.freq[val]

        if current_freq not in self.group:
            self.group[current_freq] = deque()
        self.group[current_freq].append(val)

        self.max_freq = max(self.max_freq, current_freq)

    def pop(self) -> int:
        """
        Remove and return the most frequently pushed element
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
