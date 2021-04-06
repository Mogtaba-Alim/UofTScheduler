""" This is where the week class is implemented"""
import tree
import day
from typing import Optional, List, Any


class Week:
    """ This class representes a single week in the schedule
    This class uses recursive tree data structures to store information
    """
    _week : List[day.Day]

    def __init__(self) -> None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._week = []
        for i in range(7):
            self._week.append(day.Day(days[i], []))

    def add_event_date(self, event_name: str, day_of_week: str, start_time: str, end_time: str,
                       importance: int) -> str:
        """ Adds an event to the specified time and date of the week. If the event slot is already
            filled the importance level of the current event and the new event are compared, if the
            importance level of the new event is higher than the current event the new event will
            replace the current event and the current event will be moved to the next available
            time-slot. Otherwise the new event is placed in the next available time-slot.
            - event_name: The name of the new event
            - day_of_week: A string corresponding to the day of the week of the new event
            - start_time: The time of the day corresponding to the start time of the new event.- Its
            format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - end_time: The time of the day corresponding to the end time of the new event. Its
            format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - importance: a parameter that measures the measures the importance of the event being
            inserted and is an integer between 0 and 3
        Preconditions
            - 0 <= importance <= 3
            - int(start_time[:-3]) + int(start_time[-2:]) / 100 < \
             int(end_time[:-3]) + int(end_time[-2:]) / 100
        """
        remaining_events = []
        for days in self._week:
            if days.identify_day() == day_of_week:
                remaining_events.extend(days.insert_event(event_name, importance, start_time,
                                                          end_time))
        i = 0
        new_start = "0:00"
        new_end = "0:30"
        for new_days in self._week:
            while remaining_events != [] or i != 48:













