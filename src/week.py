""" This is where the week class is implemented"""
import tree
import day
from typing import Optional, List, Any


class Week(tree.Tree):
    """ This class representes a single week in the schedule
    This class uses recursive tree data structures to store information
    """

    def __init__(self, subtrees: List[tree.Tree], root: Optional[Any] = "Week") -> None:
        super().__init__(root, subtrees)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for i in range(7):
            self.add_new_subtree(day.Day(days[i], []))

    def add_event_date(self, event_name: str, day_of_week: str, start_time: int, end_time: int,
                       importance: int) -> str:
        """ Adds an event to the specified time and date of the week. If the event slot is already
            filled the importance level of the current event and the new event are compared, if the
            importance level of the new event is higher than the current event the new event will
            replace the current event and the current event will be moved to the next available
            time-slot. Otherwise the new event is placed in the next available time-slot.
            - event_name: The name of the new event
            - day_of_week: A string corresponding to the day of the week of the new event
            - start_time: The time of the day corresponding to the start time of the new event
            - end_time: The time of the day corresponding to the end time of the new event
        """
        # for days in self._days:
        #     if days.identify_day() == day_of_week:


