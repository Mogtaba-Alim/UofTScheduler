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
        for i in range(48):
            self.create_new_subtree((str(i // 2) + ":" + str(round(i % 2) * 3) + "0",
                                     "Empty", 0))

    def identify_day(self) -> str:
        """Returns what the current day is"""
        return self._root

    def replace_event(self, event_name: str, importance: int, start: str, end: str) -> list:
        """Insert a new event into this day and return the list of the replaced or not added
         events"""
        start_int = int(start[:-3]) + int(start[-2:]) / 100
        end_int = int(end[:-3]) + int(end[-2:]) / 100
        # List of events that have been replaced or new events that were not inserted
        replaced_events = []
        for hour in self._subtrees:
            curr_event = hour.return_root()
            # breakpoint()
            curr_event_int = int(curr_event[0][:-3]) + int(curr_event[0][-2:]) / 100
            if start_int <= curr_event_int < end_int:
                if importance > int(curr_event[2]) and curr_event[1] != 'Empty':
                    replaced_events.append(curr_event)
                    hour.switch_event(curr_event[0], event_name, importance)
                elif importance > int(curr_event[2]) and curr_event[1] == 'Empty':
                    hour.switch_event(curr_event[0], event_name, importance)
                else:
                    replaced_events.insert(0, (curr_event[0], event_name, importance))

        return replaced_events

    def insert_event(self, event_name: str, importance: int, start: str, end: str) -> list:
        """Insert a new event into this day and return the list of the replaced or not added
         events. Similar to replace_event except it only inserts an event at an empty time-slot"""
        start_int = int(start[:-3]) + int(start[-2:]) / 100
        end_int = int(end[:-3]) + int(end[-2:]) / 100
        # List of events that have been replaced or new events that were not inserted
        replaced_events = []
        for hour in self._subtrees:
            curr_event = hour.return_root()
            # breakpoint()
            curr_event_int = int(curr_event[0][:-3]) + int(curr_event[0][-2:]) / 100
            if start_int <= curr_event_int < end_int:
                if importance > int(curr_event[2]) and curr_event[1] == 'Empty':
                    hour.switch_event(curr_event[0], event_name, importance)
                else:
                    replaced_events.insert(0, (curr_event[0], event_name, importance))

        return replaced_events
