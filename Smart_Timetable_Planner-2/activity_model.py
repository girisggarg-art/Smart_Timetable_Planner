"""Simple OOP Model for EL Activity 6 (Object Modeling).
Demonstrates Encapsulation (_start_min, _end_min) and Inheritance (ClassActivity, StudyActivity).
"""


class Activity:
    """Base class for any scheduled timetable activity."""

    def __init__(self, day, start, end, start_min, end_min, title, activity_type):
        self.day = day
        self.start = start
        self.end = end
        self._start_min = start_min  # Encapsulated time in minutes
        self._end_min = end_min      # Encapsulated time in minutes
        self.title = title
        self.type = activity_type

    def get_start_min(self):
        return self._start_min

    def get_end_min(self):
        return self._end_min

    def duration_hours(self):
        return (self._end_min - self._start_min) / 60.0

    def get_priority(self):
        return "Normal"

    def to_dict(self):
        return {
            "day": self.day,
            "start": self.start,
            "end": self.end,
            "title": self.title,
            "type": self.type,
        }


class ClassActivity(Activity):
    """Subclass for fixed classes and mandatory labs (inherits from Activity)."""

    def get_priority(self):
        if self.type == "lab":
            return "High (Mandatory Lab)"
        return "Medium (Fixed Class)"


class StudyActivity(Activity):
    """Subclass for flexible self-study and assignments (inherits from Activity)."""

    def get_priority(self):
        return "Low (Flexible Study)"


def make_activity(day, start, end, start_min, end_min, title, activity_type):
    """Create the right subclass object based on activity_type."""
    if activity_type in ("class", "lab"):
        return ClassActivity(day, start, end, start_min, end_min, title, activity_type)
    return StudyActivity(day, start, end, start_min, end_min, title, activity_type)
