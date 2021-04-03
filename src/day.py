""" This is where the day class is implemented"""

import tree
from typing import Optional, List, Any


class Day(tree.Tree):
    """ This class represents a single day in the schedule
    This class uses recursive tree data structures to store information
    """

    def __init__(self, root: Optional[Any], subtrees: List[tree.Tree]) -> None:
        """
        Preconditions
            - root in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', \
            'Sunday']
        """
        super().__init__(root, subtrees)
        for i in range(24):
            self.create_new_subtree((str(i) + ":00", str(i) + ":59", "Empty", 0))

    def identify_day(self) -> str:
        """Returns what the current day is"""
        return self._day.return_root()

    def insert_event(self, event_name: str, importance_level, start: int, end: int) -> str:
        """Insert a new event into this day"""
        # for hour in self._day
