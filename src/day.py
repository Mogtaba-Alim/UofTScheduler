""" This is where the day class is implemented"""

import tree


class Day:
    """ This class represents a single day in the schedule
    This class uses recursive tree data structures to store information
    Private Instance Attributes:
        - _day: A tree with trees corresponding to the hours of the day

    """
    _day = tree.Tree

    def __init__(self, day_of_week: str) -> None:
        """
        Preconditions
            - day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', \
            'Sunday']
        """
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        if day_of_week not in days:
            raise ValueError("Not a day of the week")
        self._day = tree.Tree(day_of_week, [])
        for i in range(24):
            self._day.create_new_subtree((str(i) + ":00", str(i) + ":59", "Empty", 0))

    def identify_day(self) -> str:
        """Returns what the current day is"""
        return self._day.return_root()

    def insert_event(self, event_name: str, importance_level, start: int, end: int) -> str:
        """Insert a new event into this day"""
        for hour in self._day
