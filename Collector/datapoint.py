"""
Data models for collector.
"""

from dataclasses import dataclass, field

from typing import List


@dataclass
class DataPoint:

    computer_name: str
    cpu_percentage: int
    memory_percentage: int
    timestamp: str


@dataclass
class Timeline:

    timeline: List[DataPoint] = field(default_factory= list)
    maxsize: int = 0

    def append(self, datapoint):
        if self.maxsize != 0:
            if self.maxsize <= len(self.timeline):
                self.timeline.pop(0)
        self.timeline.append(datapoint)

    def clear(self):
        self.timeline = []

    def range(self, i, j):
        return self.timeline[i:j]
