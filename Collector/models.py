"""
Data models for collector.
"""

from dataclasses import dataclass, field

from typing import List


@dataclass
class DataPoint:
    """
    A single point in the Timeline.
    """

    computer_name: str
    cpu_percentage: int
    memory_percentage: int
    timestamp: str


@dataclass
class Timeline:
    """
    A timeline of data that drops the oldest data point object
    if the maxsize is reached before inserting a new data point.
    """

    timeline: List[DataPoint] = field(default_factory= list)
    maxsize: int = 0

    def append(self, datapoint):
        """
        Add new data point object to timeline.
        """
        if self.maxsize != 0:
            if self.maxsize <= len(self.timeline):
                self.timeline.pop(0)
        self.timeline.append(datapoint)

    def clear(self):
        """
        Empties the collection.
        """
        self.timeline = []

    def latest(self):
        """
        Returns the front most data point object in the list.
        """
        if len(self.timeline) == 0:
            return None
        return self.timeline[len(self.timeline) - 1]
