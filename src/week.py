""" This is where the week class is implemented"""
import tree
import day
from typing import Optional, List, Any


class Week:
    """ This class representes a single week in the schedule
    This class uses recursive tree data structures to store information
    """
    _week: List[day.Day]

    def __init__(self) -> None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._week = []
        for i in range(7):
            self._week.append(day.Day(days[i], []))

    def add_event_date(self, event_name: str, target_day: str, start_time: str, end_time: str,
                       importance: int) -> str:
        """ Adds an event to the specified time and date of the week. If the event slot is already
            filled the importance level of the current event and the new event are compared, if the
            importance level of the new event is higher than the current event the new event will
            replace the current event and the current event will be moved to the next available
            time-slot. Otherwise the new event is placed in the next available time-slot.
            - event_name: The name of the new event
            - target_day: A string corresponding to the day of the week of the new event
            - start_time: The time ofC the day corresponding to the start time of the new event.- Its
            format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - end_time: The time of the day corresponding to the end time of the new event. Its
            format is a string looking like this: "18:00" or "3:30" with 30 minutes intervals
            - importance: a parameter that measures the measures the importance of the event being
            inserted and is an integer between 0 and 3
        Preconditions
            - 0 <= importance <= 3
            - int(start_time[:-3]) + int(start_time[-2:]) / 100 < \
            - int(end_time[:-3]) + int(end_time[-2:]) / 100
            - target_day in {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
            'Saturday', 'Sunday'}
        """
        for day in self._week:
            # if we find our day then we can operate on it.
            if target_day == day.identify_day():
                # room for optimization, can use the half method
                for hour in day._subtrees:
                    # if its empty we can just add the event
                    if hour.return_root()[1] == 'Empty':
                        day.insert_event(event_name=event_name, start=start_time, end=end_time,
                                         importance=importance)
                    elif int(hour.return_root()[2]) < importance:
                        day.replace_event(event_name=event_name, start=start_time, end=end_time,
                                         importance=importance)
                    else:
                        return 'Invalid Operation'

    def __str__(self) -> None:
        """ Prints the current schedule"""
        s = ""
        for days in self._week:
            s += days._str_indented(0)
        return s
