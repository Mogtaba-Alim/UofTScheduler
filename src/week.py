""" This is where the week class is implemented"""
import tree
import day


class Week:
    """ This class representes a single week in the schedule
    This class uses recursive tree data structures to store information
    """
    # Private Instance Atrribute:
    #   - _days: A list with its subtrees being 7 day classes, corresponding to the days of the week
    #   - _week: week designation
    _week = int
    _days = list[day.Day]

    def __init__(self, week_number: int = 0) -> None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self._week = week_number
        self._days = []
        for i in range(7):
            self._days.append(day.Day(days[i]))

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
        for days in self._days:
            if days.identify_day() == day_of_week:


